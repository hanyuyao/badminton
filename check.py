# open the website and check if there is any fields available

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

account = ''
password = ''

driver_path = r''
driver = webdriver.Chrome(driver_path)
driver.get('http://peo.nthu.edu.tw/nthugym/login_01.php')


# fill in account and password, then click login
driver.find_element_by_id("account").send_keys(account)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath('//*[@id="Contents"]/form/table/tbody/tr[4]/td/input[1]').click()

# click ok on alert window
# wait at most 10 sec, call until() every 0.01 sec
WebDriverWait(driver, 10, 0.01).until(EC.alert_is_present()).accept()

# click 一樓羽球館
time.sleep(1)
driver.find_element(By.LINK_TEXT, '一樓  羽球場').click()

time.sleep(1000)
driver.close()