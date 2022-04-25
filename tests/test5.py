import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# Test Case Description --> User allows geolocation and clicks get location button
s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.geolocation": 1}
)
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
driver.get("https://cs458pno3.netlify.app/")
driver.find_element(By.ID, "getLocation").click()

try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "toast-message")))

    assert (
            "km" in driver.find_element(By.ID, "distancePole").text
            and "km" in driver.find_element(By.ID, "distanceMoon").text
            and driver.find_element(By.ID, "countryName").text != "The country name is: "
            and driver.find_element(By.CLASS_NAME, "toast-message").text == "Successfully calculated!"
    )
    print("Test is passed")
except AssertionError:
    print("Test is failed")

driver.close()


