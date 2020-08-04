from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

date = '20200807'
time_slot = 16          # 18=18:00, 10=10:00, can't sanp fields earlier than 10 a.m.
start_field = 1         # 1 = field 1, 5 = field 5
end_field = 8           # total 1-8 fields
num_field = 2           # how many fields to reserve (maximum = 2)
account = ''
password = ''

driver_path = r''
driver = webdriver.Chrome(driver_path)
driver.get('http://peo.nthu.edu.tw/nthugym/login_01.php')

# modify variables
time_slot_org = str(time_slot)
time_slot = str(time_slot-4)
start_field += 1
end_field += 1

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

# wait until specified hour
while time.strftime('%H', time.localtime()) != time_slot_org:
    pass

driver.refresh()

while True:
    # select a date
    WebDriverWait(driver, 10, 0.01).until(EC.frame_to_be_available_and_switch_to_it(0))
    driver.find_element(By.CSS_SELECTOR, 'div[dyc-date="' + date + '"]').click()

    # switch to reservation frame
    WebDriverWait(driver, 10, 0.01).until(EC.frame_to_be_available_and_switch_to_it("ww"))      # iframe id = 'ww'

    # wait for loading elements
    path = '/html/body/table/tbody/tr[' + time_slot + ']/td[' + str(start_field) + ']'
    WebDriverWait(driver, 10, 0.01).until(EC.presence_of_element_located((By.XPATH, path)))

    # check if it is available to reserve fields
    if driver.find_elements_by_xpath(path + '/input'):              # return empty list if nothing found
        break
    else: driver.refresh()


# reserve field
for i in range(start_field, end_field+1):
    path = '/html/body/table/tbody/tr[' + time_slot + ']/td[' + str(i) + ']/input'
    element = driver.find_element_by_xpath(path)
    if element.get_attribute('value') == "我要預約":
        element.click()
        WebDriverWait(driver, 10, 0.01).until(EC.alert_is_present()).accept()
        WebDriverWait(driver, 10, 0.01).until(EC.alert_is_present()).accept()
        num_field -= 1
    if num_field == 0: break

# switch to default frame
driver.switch_to.default_content()

# click 場地管理, click 查詢預約記錄
driver.find_element(By.LINK_TEXT, '場地管理').click()
driver.find_element(By.LINK_TEXT, '查詢預約記錄').click()
time.sleep(1000)
driver.close()