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
driver.find_element(By.ID,"item-5").click()# Links sekmesine tıkla
driver.find_element(By.ID,"no-content").click()
time.sleep(1)
sonuc = driver.find_element(By.ID,"linkResponse").text
time.sleep(2)

if "204 and status text No Content" in sonuc:
    print("Test Basarili")
else:
    print("Test Basarisiz")
    
