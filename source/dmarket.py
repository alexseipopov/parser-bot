import time
import json
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .helpers import check_first

def parse_dmarket(driver, buff):
    '''Взять json-файл и поэлементно проверить 
    графики на steam -> json-файл с отфильтрованными 
    скинами
    '''

    # #onesignal-slidedown-cancel-button  - модальное
    # #mat-dialog-0 > onboarding-dialog > div > div.c-dialogHeader > div > button - всплывающее

    driver.get('https://dmarket.com/ru/ingame-items/item-list/csgo-skins')
    time.sleep(5)
    try:
        driver.execute_script('var k = document.querySelector("#onesignal-slidedown-cancel-button"); k.click()')
        time.sleep(3)
    except:
        pass
    try:
        driver.execute_script('var k = document.querySelector("#mat-dialog-0 > onboarding-dialog > div > div.c-dialogHeader > div > button"); k.click()')
        time.sleep(3)
    except:
        pass
    b = time.time()
    action = webdriver.ActionChains(driver)
    result_dmarket= {}
    
    with open(buff) as file:
        data = json.load(file)

        for id in data:
            print(f'current id is {id}')
            
            k = 0
            floats = []
            prices = []
            name = data[id]['name']
            exterior = data[id]['exterior']
            name = name.replace(' ', '%20')
            name = name.replace('|', '%7C')
            exterior = exterior.lower()
            exterior = exterior.replace(' ', '%20')
            price_from = round(data[id]['price']*1.1, 2)
            price_to = round(data[id]['price']*1.5, 2)

            list_of_prices = []
            if not data[id]['sticker'] and not data[id]['stattrak']:
                driver.get(f'https://dmarket.com/ru/ingame-items/item-list/csgo-skins?exterior={exterior}&category_0=not_stattrak_tm&category_1=not_souvenir&price-to={price_to}&price-from={price_from}&title={name}')
                check_first(driver)
                elem = driver.find_element(By.CLASS_NAME, 'c-exchange__inventory')
                #action.move_to_element(elem).perform()
                time.sleep(10)
                y = 500
                
                # for k in range(10):
                #     if  k is not 0:
                #         action.scroll(0, 0, 0, y, duration=2, origin=elem).perform()
                #         time.sleep(4)
                cards = driver.find_elements(by=By.CLASS_NAME, value='c-asset__inner')
                if cards:
                    prices.append(1)
                #     if not cards:
                #         continue
                #     for card in cards:
                        
                #         try:
                #             card.find_element(By.CLASS_NAME, 'c-asset__stickersImg')
                #             continue
                #         except:
                #             pass
                #         try:
                #             price_ = card.find_element(by=By.CSS_SELECTOR, value='price.ng-star-inserted').text
                #             float_ = card.find_element(By.CSS_SELECTOR, 'span[data-tooltip-origin-id="assetFloatNumber"]').text
                #             if float in floats:
                #                 continue
                #             floats.append(float_)
                #             price_ = price_.replace(' ','')
                #             price_ = price_.replace('$','')
                #             price_ = float(price_)
                #             prices.append(price_)
                            
                #         except:
                #             pass
                    
            elif data[id]['sticker'] and not data[id]['stattrak']:
                
                driver.get(f'https://dmarket.com/ru/ingame-items/item-list/csgo-skins?exterior={exterior}&category_0=not_stattrak_tm&category_1=not_souvenir&price-from={price_from}&title={name}')
                check_first(driver)
                elem = driver.find_element(By.CLASS_NAME, 'c-exchange__inventory')
                #action.move_to_element(elem).perform()
                time.sleep(10)
                y = 500
                cards = driver.find_elements(by=By.CLASS_NAME, value='c-asset__inner')
                if cards:
                    prices.append(1)
                # for k in range(10):
                #     if  k is not 0:
                #         action.scroll(0, 0, 0, y, duration=2, origin=elem).perform()
                #         time.sleep(4)
                #     cards = driver.find_elements(by=By.CLASS_NAME, value='c-asset__inner')
                #     if not cards:
                #         continue
                #     for card in cards:
                        
                #         try:
                #             card.find_element(By.CLASS_NAME, 'c-asset__stickersImg')
                            
                #         except:
                #             continue
                #         try:
                #             price_ = card.find_element(by=By.CSS_SELECTOR, value='price.ng-star-inserted').text
                #             float_ = card.find_element(By.CSS_SELECTOR, 'span[data-tooltip-origin-id="assetFloatNumber"]').text
                #             if float in floats:
                #                 continue
                #             floats.append(float_)
                #             price_ = price_.replace(' ','')
                #             price_ = price_.replace('$','')
                #             price_ = float(price_)
                #             prices.append(price_)
                #         except:
                #             pass
            elif not data[id]['sticker'] and data[id]['stattrak']:
                
                driver.get(f'https://dmarket.com/ru/ingame-items/item-list/csgo-skins?exterior={exterior}&category_0=stattrak_tm&category_1=not_souvenir&price-to={price_to}&price-from={price_from}&title={name}')
                check_first(driver)
                elem = driver.find_element(By.CLASS_NAME, 'c-exchange__inventory')
                #action.move_to_element(elem).perform()
                time.sleep(10)
                y = 500
                cards = driver.find_elements(by=By.CLASS_NAME, value='c-asset__inner')
                if cards:
                    prices.append(1)
                # for k in range(10):
                #     if  k is not 0:
                #         action.scroll(0, 0, 0, y, duration=2, origin=elem).perform()
                #         time.sleep(4)
                #     cards = driver.find_elements(by=By.CLASS_NAME, value='c-asset__inner')
                #     if not cards:
                #         continue
                #     for card in cards:
                        
                #         try:
                #             card.find_element(By.CLASS_NAME, 'c-asset__stickersImg')
                #             continue
                #         except:
                #             pass
                #         try:
                #             price_ = card.find_element(by=By.CSS_SELECTOR, value='price.ng-star-inserted').text
                #             float_ = card.find_element(By.CSS_SELECTOR, 'span[data-tooltip-origin-id="assetFloatNumber"]').text
                #             if float in floats:
                #                 continue
                #             floats.append(float_)
                #             price_ = price_.replace(' ','')
                #             price_ = price_.replace('$','')
                #             price_ = float(price_)
                #             prices.append(price_)
                #         except:
                #             pass
            else:
                
                driver.get(f'https://dmarket.com/ru/ingame-items/item-list/csgo-skins?exterior={exterior}&category_0=stattrak_tm&category_1=not_souvenir&price-from={price_from}&title={name}')  
                check_first(driver)    
                elem = driver.find_element(By.CLASS_NAME, 'c-exchange__inventory')
                action.move_to_element(elem).perform()
                time.sleep(10)
                y = 500
                cards = driver.find_elements(by=By.CLASS_NAME, value='c-asset__inner')
                if cards:
                    prices.append(1)
                # for k in range(10):
                #     if  k is not 0:
                #         action.scroll(0, 0, 0, y, duration=2, origin=elem).perform()
                #         time.sleep(4)
                #     cards = driver.find_elements(by=By.CLASS_NAME, value='c-asset__inner')
                #     if not cards:
                #         continue
                #     for card in cards:
                        
                #         try:
                #             card.find_element(By.CLASS_NAME, 'c-asset__stickersImg')
                            
                #         except:
                #             continue
                #         try:
                #             price_ = card.find_element(by=By.CSS_SELECTOR, value='price.ng-star-inserted').text
                #             float_ = card.find_element(By.CSS_SELECTOR, 'span[data-tooltip-origin-id="assetFloatNumber"]').text
                #             if float in floats:
                #                 continue
                #             floats.append(float_)
                #             price_ = price_.replace(' ','')
                #             price_ = price_.replace('$','')
                #             price_ = float(price_)
                #             prices.append(price_)
                #         except:
                #             pass
            if len(prices)>0:
                persent = len(prices) // 2
                sum = 0
                l = 0
                for j in prices[-persent:]:
                    sum += j
                    l+=1
                sum = round(sum/l, 2)

                print(f'\n List of Prices \n {prices} \n sum is {sum}')
                print(name, exterior,  data[id]['price'], price_from, price_to)
            # if data[id]['stattrak']:
            #     driver.get(f'https://dmarket.com/ru/ingame-items/item-list/csgo-skins?exterior={exterior}&category_0=stattrak_tm&category_1=not_souvenir&price-to={price_to}&price-from={price_from}&title={name}')
                
            # else:
            #     driver.get(f'https://dmarket.com/ru/ingame-items/item-list/csgo-skins?exterior={exterior}&category_0=not_stattrak_tm&category_1=not_souvenir&price-to={price_to}&price-from={price_from}&title={name}')
            
            # time.sleep(2)
            # cards = driver.find_elements(by=By.CLASS_NAME, value='c-asset__inner')
            # print(f'found {len(cards)} cards')
                card_dict={}
            # flag = False
            # if not cards:
            #     continue
            # else:
            #     if not data[id]['sticker']:
            #         flag = True
            #     else:
            #         for i in cards[:15]:
            #             try:
            #                 i.find_element(By.CLASS_NAME, 'c-asset__stickersImg')
            #                 flag = True
            #                 break
            #             except:
            #                 pass
                
            #     if flag:
                card_dict.setdefault('name', data[id]['name'])
                card_dict.setdefault('price', data[id]['price'])
                card_dict.setdefault('float', data[id]['float'])
                card_dict.setdefault('exterior', data[id]['exterior'])
                card_dict.setdefault('link_lis_skins', data[id]['link_lis_skins'])
                card_dict.setdefault('sticker', data[id]['sticker'])
                card_dict.setdefault('stattrak', data[id]['stattrak'])
                card_dict.setdefault('price_dmarket', sum)
                try:
                    card_dict.setdefault('time_of_unlock', data[id]['time_of_unlock'])
                except:
                    pass
                result_dmarket.setdefault(id, card_dict)
                
            # card_dict={}
            # for card in cards[:3]:
            else:
                pass
                
            #     price = card.find_element(by=By.CSS_SELECTOR, value='price.ng-star-inserted').text.replace('$','')
                
            #     dif = round(float(price) / data[id]['price'], 1)
            #     float_ = card.find_element(by=By.CSS_SELECTOR, value='span.o-blur').text

            #     # print(j, result[i]['name'], float_, price)

            #     card_dict.setdefault('name', data[id]['name'])
            #     card_dict.setdefault('price', price)
            #     card_dict.setdefault('dif',dif)
            #     card_dict.setdefault('float', float_)
            #     card_dict.setdefault('exterior', data[id]['exterior'])
            #     card_dict.setdefault('stattrak', data[id]['stattrak'])
            #     try:
            #         card_dict.setdefault('time_of_unlock', data[id]['time_of_unlock'])
            #     except:
            #         pass
            #     result_dmarket.setdefault(id, card_dict)
                
            #     k += 1
        date = datetime.datetime.now()
        buff = f'result_dmarket_{date.day}_{date.month}_{date.year}_{date.hour}-{date.minute}.json'
        with open(buff, 'w') as new_file:
            json.dump(result_dmarket, new_file, indent=4)
        a = time.time()
        print(f'Success in {a-b}')
        return buff
    