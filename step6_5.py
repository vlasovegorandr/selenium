from selenium import webdriver
import math
import time

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/find_link_text')
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = driver.find_element_by_link_text(link_text)
link.click()

input1 = driver.find_element_by_tag_name('input')
input1.send_keys('vova')
input2 = driver.find_element_by_name('last_name')
input2.send_keys('putin')
input3 = driver.find_element_by_class_name('city')
input3.send_keys('moskva')
input4 = driver.find_element_by_id('country')
input4.send_keys('rossiya')
button = driver.find_element_by_css_selector('button.btn')
button.click()

time.sleep(30)
driver.quit()
