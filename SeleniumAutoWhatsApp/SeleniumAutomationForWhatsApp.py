import datetime as dt
import random
import json
import os
import requests
import shutil
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

dir_browser = "pathto\\chromedriver.exe"

def browser_anonimo():
    options = webdriver.ChromeOptions()
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")
    options.add_argument("window-size=1280,720")
    options.add_argument(
        r"user-data-dir={}".format(profile))
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/99.0.4844.84 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(options=options, executable_path=dir_browser)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """

    Object.defineProperty(navigator, 'webdriver', {

    get: () => undefined

    })

    """

    })
    browser.execute_cdp_cmd('Network.setUserAgentOverride',

                            {
                                "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                             'like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    return browser

def pegar_contador():
    arquivo = open(os.getcwd()+"\\contador", 'r')
    linhas = arquivo.read()
    return int(linhas)

driver = browser_anonimo()

wait = WebDriverWait(driver, 30)

sleep(5)

driver.get("https://web.whatsapp.com")

df = pd.read_excel("")

caminho_para_imagem = ""
imagem = True

try:
    i = pegar_contador()
except:
    with open(os.getcwd()+"\\contador", 'w') as f:
        f.write(f'{0}')

wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/header')))

while(len(df) >= i):
    
    if (dt.datetime.now().hour - 3) == 19:
        exit(1)

    with open(os.getcwd()+"\\contador", 'w') as f:
        f.write(f'{i}')

    numero = df["Numero"].iloc[i]
    ddd = df["DDD"].iloc[i]

    driver.get(f'https://api.whatsapp.com/send?phone=55{ddd}9{numero}')

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="action-button"]'))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fallback_block"]/div/div/h4[2]/a'))).click()

    if imagem:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@title = "Anexar"]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))
        image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        sleep(1)
        image_box.send_keys(caminho_para_imagem)
        wait.until(EC.presence_of_element_located((By.XPATH, './/*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]')))
        sleep(1)
        caixaimagem = driver.find_element_by_xpath('.//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]')    
    else:
        pass

    sleep(1)

    frase_desejada = ''
    
    for palavra in frase_desejada:
        sleep(random.uniform(0.05, 0.10))
        caixaimagem.send_keys(palavra)
            
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div'))).click()
    sleep(5)
    i += 1
