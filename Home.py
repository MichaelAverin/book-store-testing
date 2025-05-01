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
options.add_extension("adblocker.crx")

# объекты
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

# локаторы
SELENIUM_RUBY = ("xpath", "//h3[text()='Selenium Ruby']")
REVIEWS_BUTTON = ("xpath", "//li[@class='reviews_tab']/a")
STARS_5_BUTTON = ("xpath", "//a[@class='star-5']")
REVIEW_FIELD = ("xpath", "//textarea")
NAME_FIELD = ("xpath", "//input[@id='author']")
EMAIL_FIELD = ("xpath", "//input[@id='email']")
SUBMIT_BUTTON = ("xpath", "//input[@id='submit']")

BASE_URL = "https://practice.automationtesting.in/"
driver.get(BASE_URL)
driver.execute_script("window.scrollTo(0, 600);")

wait.until(EC.element_to_be_clickable(SELENIUM_RUBY)).click()
wait.until(EC.element_to_be_clickable(REVIEWS_BUTTON)).click()
wait.until(EC.element_to_be_clickable(STARS_5_BUTTON)).click()
wait.until(EC.element_to_be_clickable(REVIEW_FIELD)).send_keys("Nice book!")
wait.until(EC.element_to_be_clickable(NAME_FIELD)).send_keys("Samuil")
wait.until(EC.element_to_be_clickable(EMAIL_FIELD)).send_keys("samuil@yandex.ru")
wait.until(EC.element_to_be_clickable(SUBMIT_BUTTON)).click()
