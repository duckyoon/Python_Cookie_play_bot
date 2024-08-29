from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading
import math



def cookie_number():
    money = driver.find_element(By.ID, "money")
    return int(money.text)
    
cookie_url = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(cookie_url)

cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute('id') for item in items]


time_out = time.time() + 5
close_time = time.time() + 5 * 60
end = False
while not end: 
    
    cookie.click()
    time.sleep(0.1)
    
    if time.time() > time_out:
        
        # get item price
        prices = driver.find_elements(By.CSS_SELECTOR,("#store b"))
        item_prices = []
        for price in prices:
            if price.text != "":
                price = int(price.text.split("-")[1].strip().replace(",",""))
                item_prices.append(price)
               
        # cookie upgrade
        cookie_upgrade = {}
        for n in range(len(item_prices)):
            cookie_upgrade[item_prices[n]] = item_ids[n]
             
        # get cookie number
        money = cookie_number()
        print(money)
        
        # 업그레이드 가능한 아이템 찾기
        affordable_upgrades = {}
        for cost, id in cookie_upgrade.items():
            if money > cost:
                affordable_upgrades[cost] = id
                
        # 가장 비싼 업그레이드 찾기
        most_expensive_affordable_price = max(affordable_upgrades)
        print(most_expensive_affordable_price)
        purchase_id = affordable_upgrades[most_expensive_affordable_price]
        
        driver.find_element(By.ID,purchase_id).click()

        time_out += 5
    
    if time.time() > close_time:
        cps = driver.find_element(By.ID,"cps").text
        print(cps)
        end = True
    
driver.quit()
print("Game Over")



