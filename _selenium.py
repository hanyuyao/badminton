from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, datetime

driver_path = r''
driver = webdriver.Chrome(driver_path)

driver.get('http://www.google.com')
print(driver.title)
exit(0)

# find element
# https://selenium-python.readthedocs.io/locating-elements.html
obj = driver.find_element(by=By.ID, value="TargetID")               # by id
obj = driver.find_element(By.NAME, "IamBanana")                     # by name
obj = driver.find_element(By.LINK_TEXT, "https://rootttt.com.tw")   # by link
obj = driver.find_element(By.CSS_SELECTOR, "#car span.blue.wow")    # by css selector

# run javascript
driver.execute_script("alert(1)")

# fill in data
driver.find_element_by_id("username").send_keys("USERNAME")

# click button
driver.find_element_by_id("buttom1").click()

# switch windows
driver.switch_to.window("windowName")

driver.back()           # previous page
driver.forward()        # next page
driver.refresh()        # refresh

driver.close()