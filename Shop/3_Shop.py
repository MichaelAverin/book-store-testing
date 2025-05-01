import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv
load_dotenv()

# опции браузера
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation")
options.add_extension("../adblocker.crx")

# объекты
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# локаторы
MY_ACCOUNT_BUTTON = ("xpath", "//li[@id='menu-item-50']/a")
L_EMAIL_FIELD = ("xpath", "//input[@id='username']")
L_PASSWORD_FIELD = ("xpath", "//input[@id='password']")
LOGIN_BUTTON = ("xpath", "//input[@name='login']")
WELCOME_MESSAGE = ("xpath", "//div[@class='woocommerce-MyAccount-content']")
SHOP_BUTTON = ("xpath", "//li[@id='menu-item-40']/a")
SELECTOR = ("xpath", "//select")

BASE_URL = "https://practice.automationtesting.in/"
driver.get(BASE_URL)

wait.until(EC.element_to_be_clickable(MY_ACCOUNT_BUTTON)).click()
username_field = driver.find_element(*L_EMAIL_FIELD)
username_field.send_keys(os.environ["LOGIN"])
password_field = driver.find_element(*L_PASSWORD_FIELD)
password_field.send_keys(os.environ["PASSWORD"])
wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
wait.until(EC.visibility_of_element_located(WELCOME_MESSAGE))
wait.until(EC.element_to_be_clickable(SHOP_BUTTON)).click()

title_sort = wait.until(EC.visibility_of_element_located(SELECTOR))
assert title_sort.get_attribute("value") == "menu_order", "Атрибут не соответствует"

dropdown = Select(title_sort)
dropdown.select_by_value("price-desc")

title_sort2 = wait.until(EC.visibility_of_element_located(SELECTOR))
assert title_sort2.get_attribute("value") == "price-desc", "Атрибут не соответствует"