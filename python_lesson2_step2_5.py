
from selenium import webdriver
import time
import os
   

try:
 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input2 = browser.find_element_by_name("firstname").send_keys("Potapov")
    input3 = browser.find_element_by_name("lastname").send_keys("Sergey")
    input4 = browser.find_element_by_name("email").send_keys("Potapov@mail.ru")
    current_dir = os.path.abspath(os.path.dirname("selenium_course"))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)
    input6 = browser.find_element_by_class_name("btn").click()
    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()