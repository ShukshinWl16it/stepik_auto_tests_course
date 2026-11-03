
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем кнопку, которая вызывает confirm
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 2. Принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # 3. На новой странице решаем капчу
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()
