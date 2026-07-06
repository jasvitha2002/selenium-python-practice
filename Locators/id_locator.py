import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element('id','name').send_keys('Senorita')
driver.find_element('id','email').send_keys('Senorita143@gmail.com')
time.sleep(3)
