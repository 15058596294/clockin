from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get('https://weixine.ustc.edu.cn/2020/login')
driver.find_element_by_class_name('btn').click()
emailElem=driver.find_element_by_id('username')
emailElem.send_keys('PB19000052')
emailElem=driver.find_element_by_id('password')
emailElem.send_keys('fjh123654hjf')
time.sleep(5)
driver.find_element_by_id('login').click()
time.sleep(15)
driver.find_element_by_id('report-submit-btn').click()