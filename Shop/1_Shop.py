import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
BOOK_BUTTON = ("xpath", "(//a[@class='woocommerce-LoopProduct-link'])[3]")
H1_BOOK = ("xpath", "//h1")

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
wait.until(EC.element_to_be_clickable(BOOK_BUTTON)).click()

title_text = wait.until(EC.visibility_of_element_located(H1_BOOK))
assert title_text.text == "HTML5 Forms", "Заголовок не соответствует"