
import json
from time import time
import datetime

import datetime

from currency_converter import CurrencyConverter
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from .helpers import time_of_unlock



#@time_count
def parse_lis_skins(link:str, driver):
    '''Берем ссылку 
    lis-skins.ru. Запускаем парсер. -> json-файл с 
    каталогом скинов
    '''
    before = time()
    driver.get(link)

    #Итоговый словарь для формирования json файла
    result = {}
    next_page = True
    iterator = 0
    while next_page:
        cards = driver.find_elements(by=By.CLASS_NAME, value='item')
        soup = BeautifulSoup(driver.page_source, 'lxml')
        elements = soup.find_all('div', class_="item")
        trys = 0
        for card in cards:
            card_dict={}

            id = card.get_attribute('class').split('_')[-1]
            name = card.find_element(by=By.CLASS_NAME, value='name-inner').text
            float_ = card.find_element(by=By.CSS_SELECTOR, value='.skin-info>.info-item:last-child').text
            link_ = card.find_element(By.CLASS_NAME, 'name').get_attribute('href')
            price = elements[trys].find('div', class_='price').get_text()
            exterior = elements[trys].find('div', class_='name-exterior').get_text()[1:-1]
            
            c = CurrencyConverter()
            price = round(c.convert(float(price.replace(' ', '')), 'RUB', 'USD'),3)

            card_dict.setdefault('name', name)
            card_dict.setdefault('price', price)
            card_dict.setdefault('float', float_)
            card_dict.setdefault('exterior', exterior)
            card_dict.setdefault('link_lis_skins', link_)

            try:
                sticker = card.find_element(By.CLASS_NAME, 'sticker')
                card_dict.setdefault('sticker', True)
            except:
                card_dict.setdefault('sticker', False)


            try:
                st = card.find_element(by=By.CLASS_NAME, value='stattrak')
                card_dict.setdefault('stattrak', True)
            except:
                card_dict.setdefault('stattrak', False)
            
            try:
                dtu = card.find_element(by=By.CLASS_NAME, value='hold').text.split()
                number_ = dtu[0]
                param_ = dtu[1].replace(' ', '')

                if param_=='часов':
                    card_dict.setdefault('time_of_unlock', time_of_unlock())
                elif param_ == 'дня':
                    if int(number_) == 2:
                        card_dict.setdefault('time_of_unlock', time_of_unlock()+86400)
                    if int(number_) == 3:
                        card_dict.setdefault('time_of_unlock', time_of_unlock()+86400*2)
            except:
                pass
            
            result.setdefault(id, card_dict)
            trys += 1

        next_page_button = driver.find_element(by=By.CSS_SELECTOR, value="#pagination>a:nth-last-child(2)").text
        print(next_page_button)
        if next_page_button == 'след.':
            print(f'{link}&page={iterator + 2}')
            driver.get(f'{link}&page={iterator + 2}')
        else:
            next_page = False
        iterator += 1

    # result_[hours]-[minutes]_[date]_[month]_[year]
    date = datetime.datetime.now()
    buff = f'result_{date.day}_{date.month}_{date.year}_{date.hour}-{date.minute}.json'
    with open(buff, 'w') as file:
        print(type(result))
        json.dump(result, file, indent=4)

    print('Success!!')
    after = time()
    print(round(after-before, 4))
    return buff