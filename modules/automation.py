#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import selenium

Browser = webdriver.Firefox(executable_path = f'{os.getcwd()}/geckodriver')
Browser.maximize_window()

def sign_in(username, password):
    Browser.get('https://www.instagram.com/')
    sleep(5)
    Browser.find_element(By.XPATH, "/html/body/div[1]/div/div/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
    Browser.find_element(By.XPATH, "/html/body/div[1]/div/div/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
    sleep(0.5)
    Browser.find_element(By.XPATH,"/html/body/div[1]/div/div/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
    sleep(10)

    try:
        Browser.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    except:
        print("Tardó demasiado")
        pass

#Xpath no funciona, css_selector no funciona con las sugerencias verticales
def follow():
    for x in range(3, 16):
        try:
            Browser.find_element(By.CSS_SELECTOR, f"div._8Rm4L > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child({x}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(5)").click()
            sleep(2)
        except selenium.common.exceptions.ElementClickInterceptedException:
            Browser.get("https://www.instagram.com")
            sleep(5)
        except:
            pass
        Browser.get("https://www.instagram.com")
        sleep(5)
