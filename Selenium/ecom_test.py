from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


import time



driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:3000/')
time.sleep(10)
admin_email= 'admin@example.com'
admin_password='123456'

driver.find_element_by_xpath('/html/body/div/div/header/div[2]/a[2]').click()
driver.find_element_by_xpath('/html/body/div/div/main/div/div/form/ul/li[4]/input').send_keys(admin_email)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/form/ul/li[5]/input').send_keys(admin_password)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/form/ul/li[6]/button').submit()
driver.find_element_by_xpath('/html/body/div/div/header/div[2]/a[3]').click()
driver.find_element_by_xpath('/html/body/div/div/header/div[1]/a').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/ul/li[1]/div/a/img').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[3]/ul/li[3]/select').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[3]/ul/li[3]/select/option[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[3]/ul/li[4]/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/form/ul/li[2]/input').send_keys("123 st")
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/form/ul/li[3]/input').send_keys("ABC")
driver.find_element_by_xpath("/html/body/div/div/main/div/div/div[2]/form/ul/li[6]/button").click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/form/ul/li[2]/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/form/ul/li[3]/button').submit()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div/div/main/div/div/div[2]/div[2]/ul/li[1]/button').click()












