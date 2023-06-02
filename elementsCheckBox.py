from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/") # https://demoqa.com'a git

driver.maximize_window() # pencereyi büyüt.

driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div[1]/div').click() #elements sekmesine tıkla
driver.find_element(By.XPATH,'//*[@id="item-1"]').click() # check box sekmesine tıkla
driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/span/button').click()
driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[1]/span/button').click()
driver.find_element(By.CSS_SELECTOR,"#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-title").click() # yukarıdaki işlemler ile sırasıyla Home>Desktop ve Notes sekmelerini tıkla.

sonuc = driver.find_element(By.CLASS_NAME,'text-success').text # sonuç kısmından text'i çek

if "notes" in sonuc:
    print("Test Basarili")
else:
    print("Test Basarisiz")

# notes sekmesini seçtiğimiz için kontrolü bu şekilde sağladık,  test başarılı ise "Test Basarili" sonucunu terminalde göreceğiz.
