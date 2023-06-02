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
driver.find_element(By.ID,"item-4").click()# buttons sekmesine tıkla
time.sleep(2)
action = ActionChains(driver)
buttonDouble = driver.find_element(By.ID,"doubleClickBtn")
action.double_click(buttonDouble).perform() # ilk butona çift tıkla
time.sleep(1)
buttonRightClick = driver.find_element(By.ID,"rightClickBtn")
action.context_click(buttonRightClick).perform() #ikinci butona sağ tıkla
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button').click() # son butona tıkla

