from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Test Case Description --> User enters invalid latitude
s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
driver.get("https://cs458pno3.netlify.app/")
driver.find_element(By.ID, "latitude").send_keys("-91.42345")
driver.find_element(By.ID, "longitude").send_keys("65.15678")
driver.find_element(By.ID, "submitLocation").click()

try:
    WebDriverWait(driver, 3).until(EC.alert_is_present(), "Waiting for alert timed out")
    # assert alert text
    assert (
            "Please enter a valid latitude" == driver.switch_to.alert.text
    )
    print("Test is passed")
except Exception:
    print("Test is failed")
