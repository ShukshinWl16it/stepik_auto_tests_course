from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем два числа
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text

    # 2. Считаем сумму (обязательно приводим к int, потом к str)
    s = str(int(num1) + int(num2))

    # 3. Выбираем сумму в списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(s)

    # 4. Нажимаем Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

