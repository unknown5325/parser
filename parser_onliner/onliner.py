from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import matplotlib.pyplot as plt

lis = []
arr = {}

driver = webdriver.Chrome()
driver.get('https://catalog.onliner.by/mobile/apple')
wait = WebDriverWait(driver, 10)

def get_links():
    lis = []
    time.sleep(5)
    elements = driver.find_elements(By.CLASS_NAME, 'catalog-form__link_primary-additional')
    for item in elements:
        lis.append(item.get_attribute('href'))
    return lis

def get_item():
    butt = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[3]/div[3]/a')
    butt.click()


for _ in range(0, 3):
    lis += get_links()
    get_item()

try:
    for item in lis:
        if 'prices' in item:
            lis.remove(item)
except Exception:
    pass

for item in lis:
    time.sleep(2)
    driver.get(item)
    element1 = driver.find_element(By.CLASS_NAME, 'catalog-masthead__title')
    element2 = driver.find_element(By.CLASS_NAME, 'h_txt_tl0')
    arr.update({element1.text: element2.text})


lis_v = list(arr.keys())   
lis_k = list(arr.values()) 
lis_v = [str(x) for x in lis_v] 

lis_k = [int(''.join(char for char in str(x) if char.isdigit())) for x in lis_k]
fig, ax = plt.subplots(figsize=(10, 16)) 
bars = ax.barh(lis_v, lis_k, color='#2b5c8f', edgecolor='black', height=0.7)

ax.set_title('Сравнение цен на 66 моделей телефонов', fontsize=16, pad=20, fontweight='bold')
ax.set_xlabel('Цена', fontsize=12, labelpad=10)
ax.set_ylabel('Модели телефонов', fontsize=12, labelpad=10)
ax.grid(axis='x', linestyle='--', alpha=0.5)

plt.subplots_adjust(left=0.25) 
plt.tight_layout()
plt.show()