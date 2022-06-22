from time import time, sleep
from .lis_skins import parse_lis_skins
from .dmarket import parse_dmarket
from .steam import parse_steam
from selenium import webdriver
from .helpers import auth
from .buying import buying as by
from .seil import seil as sl
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def run(link:str):
    """Step 1: Берем ссылку 
    lis-skins.ru. Запускаем парсер. -> json-файл с 
    каталогом скинов

    Step 2: Взять json-файл и поэлементно проверить 
    графики на steam -> json-файл с отфильтрованными 
    скинами

    Step 3: Взять json-файл и отфильтровать по ценам

    """
    driver = webdriver.Chrome('/Users/alexsei_popov/Library/Mobile Documents/com~apple~CloudDocs/Кодабра/КУ1В-18/bot/chromedriver-2')
    # driver.get('https://dmarket.com/ru/ingame-items/item-list/csgo-skins?exterior=field-tested&category_0=stattrak_tm&category_1=not_souvenir&title=AWP%20%7C%20Mortis')

    # sleep(10)
    
    # close_ = driver.find_element(By.CLASS_NAME, 'c-dialogHeader__close')
    # close_.click()
    buff = ''
    auth(driver)
    # lis-skins
    while True:
        buff = parse_lis_skins(link, driver)
        #buff = parse_steam(driver, buff)
        buff = parse_dmarket(driver, buff)
        
        by(driver, buff)
        sl(driver, buff)
    
    
    #c = str(driver.get_cookies())
    # with open('coockies.txt', 'w') as file:
    #     file.write(c)

    #TODO наклейки

    #FIXME парсинг куков
    
    # with open('coockies.txt', 'r') as file:
    #     c = file.read()
    # print(list(c))
    # driver.add_cookie(list(c))
    
    # with open('coockies.txt', 'w') as file:
    #     file.write(c)


