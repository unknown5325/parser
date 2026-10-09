from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import matplotlib.pyplot as plt
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os


driver = webdriver.Chrome()
driver.get('https://cars.av.by/filter?brands[0][brand]=8&brands[0][model]=5865&brands[0][generation]=4439&brands[1][brand]=8&brands[1][model]=5865&brands[1][generation]=12786&page=1')

lis1 = []
lis2 = []
def get_links():
    element1 = driver.find_elements(By.CLASS_NAME, 'listing-item__price-primary')
    element2 = driver.find_elements(By.CLASS_NAME, 'listing-item__params')
    for item in element1:
        cltext1 = item.text[:-5]
        lis1.append(cltext1)

    for item in element2:
        cltext2 = item.text
        lis2.append(cltext2)

    dictt = dict(zip(lis1, lis2))
    return dictt

def click_button():
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button--default')))
    driver.execute_script('arguments[0].click();', element)

while True:
    try:
        click_button()
        time.sleep(2)
    except Exception:
        break

arr = get_links()

lis_k = arr.keys()
lis_v = arr.values()
df_1 = pd.DataFrame({'Цена' : lis_k, 'Характеристики' : lis_v})
df_1.to_csv("var.csv", index=False,  mode="a", sep=",", header=not os.path.isfile("var.csv"))
