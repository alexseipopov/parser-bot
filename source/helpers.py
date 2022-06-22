from time import time, sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

LOGIN = '_tivrus_bot_'
PASSWORD = '32322121bot'
TRADE_LINK = 'https://steamcommunity.com/tradeoffer/new/?partner=1301471718&token=1l5WMQ9_'

anchor = 1648882800

def time_of_unlock():
    global anchor
    while time() > anchor:
        anchor += 86400
    return anchor


def is_good(coef):
    return True if -6.5*(10**-5) <= coef[0] <= 6.5*(10**-5) else False

def auth(driver):
    driver.get('https://lis-skins.ru')
    print(driver.current_window_handle)
    login_button = driver.find_element(by=By.CLASS_NAME, value='loginButton')
    action = webdriver.ActionChains(driver)
    action.move_to_element(login_button).click().perform()
    sleep(7)
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_window_handle)
    print(print(driver.window_handles))
    steam_login = driver.find_element(by=By.CSS_SELECTOR, value='#steamAccountName')
    steam_login.send_keys(LOGIN)
    stem_password = driver.find_element(by=By.CSS_SELECTOR, value='#steamPassword')
    stem_password.send_keys(PASSWORD, Keys.ENTER)
    
    sleep(45)
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://dmarket.com/')
    driver.execute_script('var k = document.querySelector(".c-navigationAuth__authBtn--logIn"); k.click();')
    sleep(2)
    driver.execute_script('var k = document.querySelector("#mat-dialog-0 > auth-dialog > auth-flows > div > login-flow > div > auth-footer > div > vendor-auth-link > button"); k.click();')
    sleep(5)
    driver.execute_script('var k = document.querySelector("#imageLogin"); k.click();')
    sleep(5)

def check_first(driver):
    try:
        elem = driver.find_element(By.CSS_SELECTOR, '#onesignal-slidedown-cancel-button')
        if elem:
            driver.execute_script('var k = document.querySelector("#onesignal-slidedown-cancel-button"); k.click();')
            sleep(5)
        elem = driver.find_element(By.CSS_SELECTOR, '#mat-dialog-1 > onboarding-dialog > div > div.c-dialogHeader > div > button')
        if elem:
            driver.execute_script('var k = document.querySelector("#mat-dialog-1 > onboarding-dialog > div > div.c-dialogHeader > div > button"); k.click();')
            sleep(5)
    except:
        pass

# def compare_