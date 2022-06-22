from pickle import TRUE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def seil(driver, bu):
    i = 0
    while True:
        i += 1
        if i%2 == 1:
            driver.get('https://dmarket.com/')
                    
            # click marketplace
            driver.execute_script('var k = document.querySelector("body > app-root > mat-sidenav-container > mat-sidenav-content > div.c-app__navigationTop > app-header > header > div > div > nav > a:nth-child(2)"); k.click();')
            time.sleep(5)

            
            # click seil 
            driver.execute_script('var k = document.querySelector("body > app-root > mat-sidenav-container > mat-sidenav-content > exchange > exchange-header > div > exchange-tabs > div > exchange-tab:nth-child(4) > button"); k.click();')
            time.sleep(10)

            action = webdriver.ActionChains(driver)
            elem = driver.find_element(By.CSS_SELECTOR, 'body > app-root > mat-sidenav-container > mat-sidenav-content > exchange > div > div > user-side > div > user-inventory > assets-card-scroll > div > div > asset-card:nth-child(2)')
            try:
                elem.find_element(By.CSS_SELECTOR, '.c-asset__fadeBannerContent.c-asset__fadeBanner--gray')
            except:
                
                action.move_to_element(elem).perform()
                action.click().perform()
                #click item
                #driver.execute_script('var k = document.querySelector("body > app-root > mat-sidenav-container > mat-sidenav-content > exchange > div > div > user-side > div > user-inventory > assets-card-scroll > div > div > asset-card:nth-child(2)"); k.click()')
                time.sleep(10)

                #click Быстрая продажа
                driver.execute_script('var k = document.querySelector("body > app-root > mat-sidenav-container > mat-sidenav-content > exchange > div > div > user-side > div > flows-buttons > div > flow-button:nth-child(4) > div > dm-button > button"); k.click()')
                time.sleep(5)

                #click Продать в модальном окне
                driver.execute_script('var k = document.querySelector("mat-dialog-container > flow-dialog > flow-stepper > set-instant-price > div > div.c-dialog__footer.ng-star-inserted > div.c-dialog__buttons.c-dialog__buttons--manage > button"); k.click()')
                time.sleep(20)
                #mat-dialog-0 > flow-dialog > flow-stepper > how-to-trade-p2p-sell > div > div.c-dialog__footer > div > button
                # body > app-root > mat-sidenav-container > mat-sidenav-content > exchange > div > div > user-side > div > flows-buttons > div > flow-button.mat-tooltip-trigger.c-exchangeButtons__item.c-exchangeButtons__item--sell.ng-star-inserted > div > dm-button > button
                #input_ = driver.find_element(By.CSS_SELECTOR, '#mat-input-25')
                #FIXME TODO Брать цену из json-файла
                #input_.send_keys(0.25)
                #mat-dialog-1 > flow-dialog > flow-stepper > set-market-price > div > div.c-dialog__footer.ng-star-inserted > div.c-dialog__buttons.c-dialog__buttons--manage > button
                time.sleep(5)
                    #driver.execute_script('var k = document.querySelector("mat-dialog-container > flow-dialog > flow-stepper > set-market-price > div > div.c-dialog__footer.ng-star-inserted > div.c-dialog__buttons.c-dialog__buttons--manage > button"); k.click()')
                #mat-dialog-0 > flow-dialog > flow-stepper > deposit-assets > div > div > exchange-trades > app-trades > app-trades-pending > div > flow-step-notificator > div > div.c-dialogStatus__buttons > a > dm-button > button
                #mat-dialog-1 > flow-dialog > flow-stepper > set-market-price > div > div.c-dialog__footer.ng-star-inserted > div.c-dialog__buttons.c-dialog__buttons--manage > button
                time.sleep(10)
                driver.execute_script('var k = document.querySelector("mat-dialog-container > flow-dialog > flow-stepper > deposit-assets > div > div > exchange-trades > app-trades > app-trades-pending > div > flow-step-notificator > div > div.c-dialogStatus__buttons > a > dm-button > button"); k.click()')
                time.sleep(10)
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(10)
                driver.execute_script('var k = document.querySelector("#you_notready > div"); k.click()')
                time.sleep(10)
                driver.execute_script('var k = document.querySelector("body > div.newmodal > div.newmodal_content_border > div > div.newmodal_buttons > div.btn_green_steamui.btn_medium > span"); k.click()')
                time.sleep(10)
                driver.execute_script('var k = document.querySelector("#trade_confirmbtn"); k.click()')
                time.sleep(10)
                driver.execute_script('var k = document.querySelector("body > div.newmodal > div.newmodal_content_border > div > div.newmodal_buttons > div > span"); k.click()')
                time.sleep(5)
                driver.switch_to.window(driver.window_handles[0])
                
                while True:
                    try:
                        elem = driver.find_element(By.CSS_SELECTOR, 'mat-dialog-container > flow-dialog > flow-stepper > instant-sale > div > div.c-dialog__footer > div > button.c-dialog__button.o-dmButton.o-dmButton--gray.ng-star-inserted')
                        time.sleep(2)
                        break
                    except:
                        pass
                try:
                    driver.execute_script('var k = document.querySelector("mat-dialog-container > flow-dialog > flow-stepper > instant-sale > div > div.c-dialog__footer > div > button.c-dialog__button.o-dmButton.o-dmButton--green.ng-star-inserted"); k.click()')
                except:
                    pass
                time.sleep(10)
            else:
                break
        else:
            driver.get('https://dmarket.com/')
                                
            # click marketplace
            driver.execute_script('var k = document.querySelector("body > app-root > mat-sidenav-container > mat-sidenav-content > div.c-app__navigationTop > app-header > header > div > div > nav > a:nth-child(2)"); k.click();')
            time.sleep(5)

            
            # click seil 
            driver.execute_script('var k = document.querySelector("body > app-root > mat-sidenav-container > mat-sidenav-content > exchange > exchange-header > div > exchange-tabs > div > exchange-tab:nth-child(4) > button"); k.click();')
            time.sleep(10)

            #click Быстрая продажа
            driver.execute_script('var k = document.querySelector("body > app-root > mat-sidenav-container > mat-sidenav-content > exchange > div > div > user-side > div > flows-buttons > div > flow-button:nth-child(4) > div > dm-button > button"); k.click()')
            time.sleep(5)

            #click Продать в модальном окне
            try:
                driver.execute_script('var k = document.querySelector("mat-dialog-container > flow-dialog > flow-stepper > set-instant-price > div > div.c-dialog__footer.ng-star-inserted > div.c-dialog__buttons.c-dialog__buttons--manage > button"); k.click()')
            except:
                pass
            try:
                driver.execute_script('var k = document.querySelector("mat-dialog-container flow-dialog > flow-stepper > set-instant-price > div > div > flow-step-notificator > div > div.c-dialogStatus__buttons > button"); k.click()')
            except:
                pass
            time.sleep(10)

            try:
                driver.execute_script('var k = document.querySelector("mat-dialog-container > flow-dialog > flow-stepper > instant-sale > div > div.c-dialog__footer > div > button"); k.click()')
            except:
                pass
            time.sleep(5)

            try:
                
                driver.execute_script('var k = document.querySelector("mat-dialog-container > subscription-dialog > div > div.c-dialogSubscription__header > button"); k.click()')
                time.sleep(5)
            except:
                pass
            
        # while True:
        #     pass

    

    #нужен переход на вторую вкладку

    #you_notready > div - подтвержаем галочкой

    #body > div.newmodal > div.newmodal_content_border > div > div.newmodal_buttons > div.btn_green_steamui.btn_medium > span

    #trade_confirmbtn - кнопка подтверждения

    #body > div.newmodal > div.newmodal_content_border > div > div.newmodal_buttons > div > span





    #mat-dialog-0 > flow-dialog > flow-stepper > instant-sale > div > div.c-dialog__footer > div > button.c-dialog__button.o-dmButton.o-dmButton--gray.ng-star-inserted
    #mat-dialog-0 > flow-dialog > flow-stepper > instant-sale > div > div.c-dialog__footer > div > button.c-dialog__button.o-dmButton.o-dmButton--green.ng-star-inserted

    #mat-dialog-0 > flow-dialog > flow-stepper > instant-sale > div > div.c-dialog__footer > div > button


    #Крестик на попапах
    #mat-dialog-1 > subscription-dialog > div > div.c-dialogSubscription__header > button > mat-icon