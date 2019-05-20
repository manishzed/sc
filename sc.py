# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:39:28 2019

@author: hp
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def sc_test():

    # Create the Firefox web browser
    driver = webdriver.Chrome(r'C:\webdriver\chromedriver.exe')

    # Access the Django web server home page.
    driver.get('https://google.com')
    form = driver.find_element_by_name("q")
    form.send_keys("github")

    form.send_keys(Keys.ENTER)

    driver.get("https://github.com/")
    login_link = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
    login_link.click()

    id = driver.find_element_by_id("login_field")
    id.send_keys("manishkumar.zed@gmail.com")

    pw = driver.find_element_by_id("password")
    pw.send_keys("manishzed@123")

    submit = driver.find_element_by_name("commit")
    submit.click()
    
    driver.find_element_by_xpath("/html/body/div[1]/header/div[8]/details/summary").click()

    driver.find_element_by_xpath("/html/body/div[1]/header/div[8]/details/details-menu/a[1]").click()

    x=driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[1]/div[4]/h1').text
    print(x)

    
    # Close and quit the Firefox web browser
    #driver.quit()

sc_test()
