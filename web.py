from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options

def configuration():
    """
    Permet de faire la configuration nécessaire pour faire le scrapping
    :return: driver
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    path = "/usr/lib/chromedriver"
    driver = webdriver.Chrome(path,chrome_options=chrome_options)
    driver.get('https://www.youtube.com/playlist?list=PLLcJpRZdcIitBujFDiYthJwcKSSt_V37j')
    return driver
