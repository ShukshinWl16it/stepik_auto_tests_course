import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем текстовые поля
    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email.send_keys("test@test.com")

    # Загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")

    # Создаём пустой файл, если его нет
    with open(file_path, "w") as f:
        pass

    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(file_path)

    # Нажимаем Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

