from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# Test Case Description --> User enters valid latitude and longitude
s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
driver.get("https://cs458pno3.netlify.app/")
driver.find_element(By.ID, "latitude").send_keys("40.730610")
driver.find_element(By.ID, "longitude").send_keys("-73.935242")
driver.find_element(By.ID, "submitLocation").click()

try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))

    assert (
            "km" in driver.find_element(By.ID, "distancePole").text
            and "km" in driver.find_element(By.ID, "distanceMoon").text
            and "United States" in driver.find_element(By.ID, "countryName").text
            and driver.find_element(By.CLASS_NAME, "toast-message").text == "Successfully calculated!"
    )
    print("Test is passed")
except AssertionError:
    print("Test is failed")

driver.close()
