from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By


Service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=Service)





driver.get('https://www.google.com')

imput_element = driver.find_element(By.ID, 'APjFqb')
imput_element.send_keys('selenium')

time.sleep(20)

driver.close()