import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/") # https://demoqa.com'a git

driver.maximize_window() # pencereyi büyüt.

driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div[1]/div').click() #elements sekmesine tıkla
driver.execute_script("window.scrollBy(0,300)", "") # Sayfayı 300 piksel aşağı indir.
driver.find_element(By.ID,"item-3").click()# buttons sekmesine tıkla
driver.find_element(By.ID,"addNewRecordButton").click()# Add butonuna tıkla
time.sleep(2)
driver.find_element(By.ID,"firstName").send_keys("Kaya")
driver.find_element(By.ID,"lastName").send_keys("Yılmaz")
driver.find_element(By.ID,"userEmail").send_keys("kylmaz@gmail.com")
driver.find_element(By.ID,"age").send_keys(34)
driver.find_element(By.ID,"salary").send_keys(3400)
driver.find_element(By.ID,"department").send_keys("IT")
driver.find_element(By.ID,"submit").click()


