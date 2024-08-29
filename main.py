from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
import math

def purchase_item():
    try:
        if elder_pledge.is_enabled():
            elder_pledge.click()
        if time_machine.is_enabled():
            time_machine.click()
        if protal.is_enabled():
            protal.click()
        if alchemy_lab.is_enabled():
            alchemy_lab.click()
        if shipment.is_enabled():
            shipment.click()
        if mine.is_enabled():
            mine.click()
        if factory.is_enabled():
            factory.click()
        if grandma.is_enabled():
            grandma.click()
        if cursor.is_enabled():
            cursor.click()
    except:
        pass

    
cookie_url = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(cookie_url)

cookie = driver.find_element(By.ID, "cookie")
elder_pledge = driver.find_element(By.ID,"buyElder Pledge")
time_machine = driver.find_element(By.ID,"buyTime machine")
protal = driver.find_element(By.ID,"buyPortal")
alchemy_lab = driver.find_element(By.ID,"buyAlchemy lab")
shipment = driver.find_element(By.ID,"buyShipment")
mine = driver.find_element(By.ID,"buyMine")
factory = driver.find_element(By.ID,"buyFactory")
grandma = driver.find_element(By.ID,"buyGrandma")
cursor = driver.find_element(By.ID,"buyCursor")

start_time = int(time.time())
end = False
while not end: 
    cookie.click()
    time.sleep(0.1)
    end_time = int(time.time())
    elapsed_time = end_time - start_time
    if elapsed_time % 5 == 0:
        purchase_item()

    if elapsed_time > 300:
        end = True
        
driver.quit()
print("Game Over")



