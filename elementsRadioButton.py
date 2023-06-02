from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/") # https://demoqa.com'a git

driver.maximize_window() # pencereyi büyüt.

driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div[1]/div').click() #elements sekmesine tıkla
driver.find_element(By.ID,'item-2').click() # Radio box sekmesine tıkla
driver.find_element(By.CSS_SELECTOR,"#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(3) > label").click() # impressive butonunu tıkla
sonuc = driver.find_element(By.CLASS_NAME,"text-success").text #sonucu al

if "Impressive" in sonuc:
    print("Test Basarili")
else:
    print("Test Basarisiz")