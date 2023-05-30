from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

while True :
    driver = webdriver.Chrome()
    driver.minimize_window()
    driver.get("https://forum.antichat.com/")

    now = datetime.now()
    current_dt = now.strftime("%d/%m/%Y %H:%M:%S")
    now_online_user = ''

    for element in driver.find_elements(By.CLASS_NAME,"listInline"):
        now_online_user = element.text

    
    f = open("antichat.txt", "a")
    f.write(current_dt + ', ' + now_online_user + "\n")
    f.close()
    driver.close()
    
    time.sleep(60)
    

