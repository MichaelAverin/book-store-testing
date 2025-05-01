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
SHOPPING_CART = ("xpath", "//a[@class='wpmenucart-contents']")
CHECKOUT = ("xpath", "//div[@class='wc-proceed-to-checkout']//a")
FN_FIELD = ("xpath", "//input[@id='billing_first_name']")
LN_FIELD = ("xpath", "//input[@id='billing_last_name']")
EM_FIELD = ("xpath", "//input[@id='billing_email']")
PH_FIELD = ("xpath", "//input[@id='billing_phone']")
COUNTRY_SELECT = ("xpath", "//span[@id='select2-chosen-1']")
COUNTRY_CHOSE = ("xpath", "(//span[@class='select2-match' and contains (text(), 'United States')])[1]")
COUNTRY_FIELD = ("xpath", "//input[@id='s2id_autogen1_search']")
ADRESS_FIELD = ("xpath", "//input[@id='billing_address_1']")
CITY_FIELD = ("xpath", "//input[@id='billing_city']")
STATE_FIELD = ("xpath", "//div[@id='s2id_billing_state']")
STATE_SELECT = ("xpath", "//input[@id='s2id_autogen2_search']")
STATE_CHOOSE = ("xpath", "//span[@class='select2-match' and contains (text(), 'California')]")
ZIP_FIELD = ("xpath", "//input[@id='billing_postcode']")
PAY_RADIO = ("xpath", "//input[@id='payment_method_cheque']")
ORDER_BUTTON = ("xpath", "//input[@id='place_order']")
TEXT = ("xpath", "//p[text()='Thank you. Your order has been received.']")
PAY_CHECK = ("xpath", "//td[text()='Check Payments']")
LOADING = ("xpath", "(//div[contains(@class, 'blockOverlay')])[2]")

BASE_URL = "https://practice.automationtesting.in/"
driver.get(BASE_URL)

wait.until(EC.element_to_be_clickable(SHOP_BUTTON)).click()
wait.until(EC.element_to_be_clickable(ADD_BOOK_BUTTON)).click()
wait.until(EC.element_to_be_clickable(SHOPPING_CART)).click()
wait.until(EC.element_to_be_clickable(CHECKOUT)).click()
wait.until(EC.element_to_be_clickable(FN_FIELD)).send_keys("Samuil")
wait.until(EC.element_to_be_clickable(LN_FIELD)).send_keys("Ivanov")
wait.until(EC.element_to_be_clickable(EM_FIELD)).send_keys("samuil@yandex.ru")
wait.until(EC.element_to_be_clickable(PH_FIELD)).send_keys("+79991234567")
wait.until(EC.element_to_be_clickable(COUNTRY_SELECT)).click()
wait.until(EC.element_to_be_clickable(COUNTRY_FIELD)).send_keys("United States (US)")
wait.until(EC.element_to_be_clickable(COUNTRY_CHOSE)).click()
wait.until(EC.element_to_be_clickable(ADRESS_FIELD)).send_keys("Salova str.")
wait.until(EC.element_to_be_clickable(CITY_FIELD)).send_keys("St. Petersburg")
wait.until(EC.element_to_be_clickable(STATE_FIELD)).click()
wait.until(EC.element_to_be_clickable(STATE_SELECT)).send_keys("California")
wait.until(EC.element_to_be_clickable(STATE_CHOOSE)).click()
wait.until(EC.element_to_be_clickable(ZIP_FIELD)).send_keys("95899")
wait.until(EC.invisibility_of_element_located(LOADING))
radio_button = driver.find_element(*PAY_RADIO)
radio_button.click()
radio_button.is_selected()
wait.until(EC.element_to_be_clickable(ORDER_BUTTON)).click()
wait.until(EC.visibility_of_element_located(TEXT))