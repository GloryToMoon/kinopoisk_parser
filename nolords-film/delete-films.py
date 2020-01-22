how to delete repos github#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox

del_file = open('gurbage.txt','r')
del_spisok = del_file.read().split('\n')
del_spisok.pop()
del_file.close()

debug = 1 # 0 to switch off
opts = Options()
opts.set_headless()
assert opts.headless

kinch_h =[]
kinch = []
for i in del_spisok:
    kinch_h = i.split(' ')
    kinch.append(kinch_h[0])

def open_brow():
    global debug,driver,wait,x,kinch
    driver = Firefox(options=opts) # not GUI
#    driver = Firefox() # GUI
    wait = WebDriverWait(driver, 1000)
    print (kinch.index(x))
    driver.get(x)
    if debug == 1:
        print ('Браузер запустился')
def login():
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="btn-login btn js-login to-mob"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="login_name"]'))).send_keys(login)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="login_password"]'))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@title="Вход"]'))).click()

    if debug == 1:
        print ('Залогинился')
def del_news():
    wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="fedit"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[4]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"]'))).send_keys(Keys.TAB + Keys.RETURN)
    print ('Удалил')
if __name__ == '__main__':
    for x in kinch:
        login = str(input ('Login: '))
        password = str(input ('Password: '))
        open_brow()
        login()
        del_news()
        driver.close()
