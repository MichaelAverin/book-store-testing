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
ADD_BOOK_BUTTON = ("xpath", "//a[@data-product_id='182']")
SUM_CART = ("xpath", "//span[@class='cartcontents']")
PRICE_CART = ("xpath", "//span[@class='amount']")
SHOPPING_CART = ("xpath", "//a[@class='wpmenucart-contents']")
SUBTOTAL = ("xpath", "//td[@data-title='Subtotal']")
TOTAL = ("xpath", "(//td[@data-title='Total'])[2]")

BASE_URL = "https://practice.automationtesting.in/"
driver.get(BASE_URL)

wait.until(EC.element_to_be_clickable(SHOP_BUTTON)).click()
wait.until(EC.element_to_be_clickable(ADD_BOOK_BUTTON)).click()
wait.until(EC.text_to_be_present_in_element(SUM_CART, "1 Item"))
wait.until(EC.text_to_be_present_in_element(PRICE_CART, "₹180.00"))
wait.until(EC.element_to_be_clickable(SHOPPING_CART)).click()
subtotal = wait.until(EC.visibility_of_element_located(SUBTOTAL))
assert subtotal.text == "₹180.00", "Стоимость равна 180.00"
total = wait.until(EC.visibility_of_element_located(TOTAL))
assert total.text == "₹183.60", "Стоимость равна 183.60"