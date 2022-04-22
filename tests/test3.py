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
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://cs458pno3.netlify.app/")
driver.find_element(By.ID, "latitude").send_keys("40.730610")
driver.find_element(By.ID, "longitude").send_keys("-73.935242")
driver.find_element(By.ID, "submitLocation").click()
driver.implicitly_wait(5)

try:
    initial_north_pole_text = "The distance to the north pole is:"
    initial_moon_text = "The distance to the moon's core is: Calculating..."

    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, "distanceMoon"), "km")
    )

    assert (
            driver.find_element(By.ID, "distancePole").text
            != initial_north_pole_text
            and driver.find_element(By.ID, "distanceMoon").text
            != initial_moon_text
    )
    print("Test is passed")
except AssertionError:
    print("Test is failed")
