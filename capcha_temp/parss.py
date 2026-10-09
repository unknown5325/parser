from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from captcha import get_capcha


driver = webdriver.Chrome()
driver.get('https://rucaptcha.com/demo/normal')

element1 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/main/div/div/div[1]/section/div/form/div[1]/img')
element1.screenshot('capcha_temp/image.png')

element2 = driver.find_element(By.XPATH, '//*[@id="simple-captcha-field"]')
element2.clear()
element2.send_keys(get_capcha())
time.sleep(10)


element3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/main/div/div/div[1]/section/div/form/div[2]/button[1]')
element3.click()

input()
