#WRITTEN BY NILL-XD

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':


    email = "example@email.com" #EMAIL
    password = "example@@@@@@@" #PASSWORD


    options = webdriver.ChromeOptions()
    browser = uc.Chrome(options=options)

    try:
        browser.get('https://razerid.razer.com/')
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#onetrust-reject-all-handler'))
        ).click()

        email_input = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="input-login-email"]'))
        )
        email_input.send_keys(email)

        password_input = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="input-login-password"]'))
        )
        password_input.send_keys(password)

        log1n_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-log-in"]'))
        )
        log1n_button.click()

        time.sleep(10)

    except Exception as errorx:
        print(errorx)

    finally:
        browser.quit()
