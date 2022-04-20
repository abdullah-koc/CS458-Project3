from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Test Case Description --> User logs in with correct e-mail and password
s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.geolocation": 2}
)
driver = webdriver.Chrome(options=options, service=s)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://cs458pno3.netlify.app/")
driver.find_element(By.ID, "getLocation").click()
driver.implicitly_wait(2)

try:
    WebDriverWait(driver, 3).until(EC.alert_is_present(), "Waiting for alert timed out")
    print("Test is passed")
except Exception:
    print("Test is failed")
