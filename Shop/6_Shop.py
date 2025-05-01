from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
SHOP_BUTTON = ("xpath", "//li[@id='menu-item-40']/a")
ADD_BOOK1_BUTTON = ("xpath", "//a[@data-product_id='182']")
ADD_BOOK2_BUTTON = ("xpath", "//a[@data-product_id='180']")
SHOPPING_CART = ("xpath", "//a[@class='wpmenucart-contents']")
DELETE_BOOK1_BUTTON = ("xpath", "//a[@data-product_id='182']")
UNDO1 = ("xpath", "//div[@class='woocommerce-message']//a")
CHANGE = ("xpath", "(//input[@type='number'])[1]")
UPDATE = ("xpath", "//input[@value='Update Basket']")
COUPON = ("xpath", "//input[@value='Apply Coupon']")
ERROR_TEXT = ("xpath", "//li[text()='Please enter a coupon code.']")

WAIT1 = ("xpath", "//a[text()='View Basket']")
WAIT2 = ("xpath", "(//a[text()='View Basket'])[2]")
WAIT3 = ("xpath", "//h2")
WAIT4 = ("xpath", "//div[@class='woocommerce-message']")

BASE_URL = "https://practice.automationtesting.in/"
driver.get(BASE_URL)

wait.until(EC.element_to_be_clickable(SHOP_BUTTON)).click()
wait.until(EC.element_to_be_clickable(ADD_BOOK1_BUTTON)).click()
wait.until(EC.visibility_of_element_located(WAIT1))
wait.until(EC.element_to_be_clickable(ADD_BOOK2_BUTTON)).click()
wait.until(EC.visibility_of_element_located(WAIT2))
wait.until(EC.element_to_be_clickable(SHOPPING_CART)).click()
wait.until(EC.visibility_of_element_located(WAIT3))
wait.until(EC.element_to_be_clickable(DELETE_BOOK1_BUTTON)).click()
wait.until(EC.element_to_be_clickable(UNDO1)).click()
change = wait.until(EC.element_to_be_clickable(CHANGE))
change.clear()
change.send_keys("3")
wait.until(EC.element_to_be_clickable(UPDATE)).click()
check = wait.until(EC.visibility_of_element_located(CHANGE))
assert check.get_attribute("value") == "3", "Атрибут не соответствует"
wait.until(EC.visibility_of_element_located(WAIT4))
wait.until(EC.element_to_be_clickable(COUPON)).click()
wait.until(EC.visibility_of_element_located(ERROR_TEXT))