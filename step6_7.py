from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/find_xpath_form')

    input1 = driver.find_element_by_tag_name('input')
    input1.send_keys('vova')
    input2 = driver.find_element_by_name('last_name')
    input2.send_keys('putin')
    input3 = driver.find_element_by_class_name('city')
    input3.send_keys('moskva')
    input4 = driver.find_element_by_id('country')
    input4.send_keys('rossiya')

    button = driver.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(30)
    driver.quit()
    