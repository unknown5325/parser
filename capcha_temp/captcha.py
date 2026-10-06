from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_capcha():
    driver = webdriver.Chrome()
    driver.get('https://www.prepostseo.com/ru/image-to-text')
    file_inp = os.path.abspath('capcha_temp/image.png')

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
    element.send_keys(file_inp)
    time.sleep(2)


    element2 = driver.find_element(By.XPATH, '/html/body/main/section[1]/div[4]/div[3]/div[1]')
    element2.click()
    time.sleep(10)

    element3 = driver.find_element(By.XPATH, '//*[@id="result__text0"]').text
    return element3
