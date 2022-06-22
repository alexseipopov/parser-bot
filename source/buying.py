import json
import time
from .helpers import TRADE_LINK
from selenium import webdriver

from selenium.webdriver.common.by import By

def buying(driver, buff):
    

    with open(buff) as file:
        data = json.load(file)

        for id in data:
            link = data[id]['link_lis_skins']
            driver.get(link)
            time.sleep(1)
            current_balance = float(driver.find_element(By.CSS_SELECTOR, '.user_balance').text)
            if data[id]['price'] > current_balance:
                break
            
            
            time.sleep(2)
            buy_button = driver.find_element(By.CSS_SELECTOR, '.skin-min-price>.buy-button')
            buy_button.click()
            time.sleep(1)
            buy_button2 = driver.find_element(By.CSS_SELECTOR, '.cart-info>.buy-button')
            buy_button2.click()
            time.sleep(10)
            confirm_button = driver.find_element(By.CSS_SELECTOR, '.popup-center-message>.content-button>a.popup-button')
            confirm_button.click()
            time.sleep(15)

            # #FIXME Затык

            change_button = driver.find_element(By.CSS_SELECTOR, '.extra-info-cell>a.table-button')
            change_button.click()
            time.sleep(10)

            driver.switch_to.window(driver.window_handles[1])

            action = webdriver.ActionChains(driver)
            time.sleep(5)
            # # FIXME Что возможно мы не переключемся по вкладке
            driver.execute_script('var d = document.getElementById("you_notready"); d.click();')
            #change_button2 = driver.find_element(By.CSS_SELECTOR, '#you_notready>.content')
            #action.move_to_element(change_button2).perform()
            #action.click(change_button2).perform()

            time.sleep(1)
            driver.execute_script('var g = document.getElementById("trade_confirmbtn"); g.click();')
            #confirm_button3 = driver.find_element(By.CSS_SELECTOR, '#trade_confirmbtn')
            #action.move_to_element(confirm_button3).perform()
            #action.click(confirm_button3).perform()
            time.sleep(2)
            driver.execute_script('var k = document.querySelector(".receipt_buttons>div:nth-child(2)"); k.click();')
            driver.switch_to.window(driver.window_handles[0])


            

            #   #onesignal-slidedown-cancel-button
            #   #mat-dialog-1 > onboarding-dialog > div > div.c-dialogHeader > div > button

            