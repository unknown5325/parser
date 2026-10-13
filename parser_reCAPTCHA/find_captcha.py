from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def find_cap():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/recaptcha/api2/demo')
    wait = WebDriverWait(driver, 10)

    driver.switch_to.default_content()

    try:
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='anchor']")))

        checkbox = wait.until(EC.element_to_be_clickable((By.ID, "recaptcha-anchor")))
        checkbox.click()

        driver.switch_to.default_content()
        WebDriverWait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src*='bframe']")))

        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.ID, "rc-imageselect")))  
        time.sleep(1)
        
        element = driver.find_element(By.XPATH, '//body')
        element.screenshot('reCap/capcha.png')

    except TimeoutException:
        driver.switch_to.default_content()
        time.sleep(1)
        driver.save_screenshot('capcha_temp/capcha_full_page.png')
        
    finally:
        driver.quit()