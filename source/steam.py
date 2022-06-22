import json
import time
import numpy as np
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from .helpers import is_good



def parse_steam(driver, buff):
    b = time.time()
    result_steam = {}
    iter = 0
    action = webdriver.ActionChains(driver)
    with open(buff) as file:
        data = json.load(file)
        for id in data:
            print(id)
            iter += 1
            if iter > 2:
                break
            exterior = data[id]['exterior']
            if exterior == 'Field-Tested':
                exter = 'tag_WearCategory2'
            elif exterior == 'Well-Worn':
                exter = 'tag_WearCategory3'
            elif exterior == 'Battle-Scarred':
                exter = 'tag_WearCategory4'
            elif exterior == 'Minimal Wear':
                exter = 'tag_WearCategory1'
            elif exterior == 'Factory New':
                exter = 'tag_WearCategory0'

            name = data[id]['name']
            name = name.replace(' ', '+')
            name = name.replace('|', '%7C')
            driver.get(f'https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Exterior%5B%5D={exter}&appid=730&q={name}')
            time.sleep(2)
            try:
                if data[id]['stattrak']:
                    elem = driver.find_element(By.CSS_SELECTOR, 'a.market_listing_row_link>div[data-hash-name*="StatTrak"]')
                else:
                    elem = driver.find_element(By.CLASS_NAME, 'market_listing_row_link')
            except:
                continue
            action.move_to_element(elem).perform()
            action.click().perform()
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, 700)")
            canvas = driver.find_element(By.CLASS_NAME, 'jqplot-series-shadowCanvas')
            w = canvas.get_attribute('width')
            h = canvas.get_attribute('height')
            action.move_to_element(canvas).perform()
            action.move_by_offset(-round(int(w)/2)+1, -round(int(h)/2)+1)
            #action.click_and_hold()
            x=0
            all_costs = []
            all_x =[]
            for i in range(0, int(w), 10):
                x+=10
                k=0
                action.move_by_offset(10, 0).perform()
                for j in range(0, int(h), 15):
                    k+=1
                    canv = driver.find_element(By.CLASS_NAME, 'jqplot-highlighter-tooltip')
                    canv_list = canv.get_attribute('style').split(';')
                    for g in canv_list:
                        l = g.replace(' ', '')
                        itog = l.split(':')
                        if itog[0] == 'display' and itog[1] == 'block':
                            print(canv.text)
                            try:
                                cost = canv.text.split('\n')
                                print(cost)
                                cost_final = cost[1].split('$')[1]
                                print(cost_final)
                                all_costs.append(float(cost_final))
                                all_x.append(x)
                                print('ok')
                            except:
                                print('Значение пропущено')
                    action.move_by_offset(0, 15).perform()
                action.move_by_offset(0, -k*15).perform()
            coef = np.polyfit(all_x, all_costs, 2)
            
            print(coef)
            card_dict = {}
            if is_good(coef):
                print(True)
                card_dict.setdefault('name', data[id]['name'])
                card_dict.setdefault('price', data[id]['price'])
                card_dict.setdefault('float', data[id]['float'])
                card_dict.setdefault('exterior', data[id]['exterior'])
                card_dict.setdefault('link_lis_skins', data[id]['link_lis_skins'])
                card_dict.setdefault('stattrak', data[id]['stattrak'])
                card_dict.setdefault('sticker', data[id]['sticker'])
                # card_dict.setdefault('price_dmarket', data[id]['price_dmarket'])
                try:
                    card_dict.setdefault('time_of_unlock', data[id]['time_of_unlock'])
                except:
                    pass
                result_steam.setdefault(id, card_dict)
                
            else:
                print(False)
        date = datetime.datetime.now()
        buff = f'result_steam_{date.day}_{date.month}_{date.year}_{date.hour}-{date.minute}.json'
        with open(buff, 'w') as new_file:
            json.dump(result_steam, new_file, indent=4)
        return buff


    

            

    a = time.time()
    print(f'Success in {a-b}')