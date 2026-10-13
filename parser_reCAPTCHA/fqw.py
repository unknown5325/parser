from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException


# driver = webdriver.Chrome()
# options = Options()
# fst = 'Mozilla/5.0 (Windows NT 60.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36'
# options.add_argument(f'--user-agent={fst}')
# driver = webdriver.Chrome(options=options)

# driver.get('https://whatmyuseragent.com/')

# driver = webdriver.Chrome()
# options = Options()
# fst = 'http://157.20.35.18:8080'
# options.add_argument(f'--proxy-server={fst}')
# driver = webdriver.Chrome(options=options)

# driver.get('https://whatmyuseragent.com/')