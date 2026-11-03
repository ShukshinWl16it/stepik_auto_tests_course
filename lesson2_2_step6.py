import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем x и считаем функцию
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # 2. Скроллим страницу, чтобы элементы не перекрывались футером
    browser.execute_script("window.scrollBy(0, 100);")

    # 3. Вводим ответ
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    # 4. Отмечаем checkbox
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    # 5. Выбираем radiobutton
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()

    # 6. Нажимаем Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(30)
    browser.quit()

