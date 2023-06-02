import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/") # https://demoqa.com'a git

driver.maximize_window() # pencereyi büyüt.

driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div[1]/div').click() #elements sekmesine tıkla
driver.find_element(By.ID,"item-0").click() # text box sekmesine tıkla
driver.find_element(By.ID,"userName").send_keys("Kaan")# First Name alanına Kaan yaz
driver.find_element(By.ID,"userEmail").send_keys("kaan@kaangedikli.com")# Mail alanına text gir.
driver.find_element(By.ID,"currentAddress").send_keys("Sakarya") # Adres gir
driver.find_element(By.ID,"permanentAddress").send_keys("Sakarya") # İkinci adres gir.
time.sleep(1) # bir saniye bekle.
driver.execute_script("window.scrollBy(0,300)", "") # Sayfayı 300 piksel aşağı indir.
driver.find_element(By.ID,"submit").click() #Submit butonuna tıkla.
sonuc = driver.find_element(By.ID,"output").text # submit dedikten sonra gelen sonuc ekranındaki yazıları al

if "Name:Kaan" in sonuc:
    print("Test Basarili!")
else :
    print("Testte Hata Var!")
    
# eğer girdiğimiz bilgi eşleştiyse terminalde "Test Basarili" yazısını al, aksi halde "Testte Hata Var!" yazısı alacaksın.