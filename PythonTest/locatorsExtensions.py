import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service_obj=Service("C:/Users/supra/Downloads/chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")
#when u have only one tag name then u can only use//  tagname[1] for xpath where [1] is 1 st div ....by this u can traverse throgh parent to child class
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//Form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"Form div[2]/input").click()

