import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service_obj=Service("C:/Users/supra/Downloads/chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#to identify the web eelments in web page we have locators elements
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
#to create a xpath of any element tagname[@attribute="value of attribute']
driver.find_element(By.XPATH,"//input[@type='submit']").click()

#same for CCS SELECTOR tagname[tagname='value']
#driver.find_element(By.CSS_SELECTOR,"input[@type='submit']").click()
#message=driver.find_element(By.CLASS_NAME,"alert-success").text
#print(message)
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello again ")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
time.sleep(5)