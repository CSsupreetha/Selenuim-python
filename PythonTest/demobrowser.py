import time

from selenium import webdriver
# If we are useing older version of the chrme , then go to chrome web driver and download it to your folder and pass the path as a parameter to the service()
#service_object=service("path to the webdriver")
#driver = webdriver.Chrome(service=service_object)
driver = webdriver.Chrome()
driver.get("http://www.python.org")
#to maximize the window
driver.maximize_window()
#to get the title of the webpage
print(driver.title)
#to get the current url
print(driver.current_url)
#to run test on firefox webbrowser
#driver=webdriver.Firefox()
#to run test on Edge webbrowser
#driver=webdriver.Edge()
time.sleep(2)