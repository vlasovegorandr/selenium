from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/huge_form.html')
    elems = driver.find_elements_by_tag_name('input')
    for elem in elems:
        elem.send_keys('answer')

    button = driver.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(15)
    driver.quit()