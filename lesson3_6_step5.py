import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.get("https://stepik.org/login")
    
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "id_login_email"))
    ).send_keys("vovaschukshin@yandex.ru")
    browser.find_element(By.ID, "id_login_password").send_keys("Vladimir7788)")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(5)
    
    yield browser
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_collect_message(browser, link):
    print(f"\n--- {link} ---")
    try:
        browser.get(link)
        time.sleep(3) 

        # Сброс
        try:
            reset_btn = browser.find_element(By.XPATH, "//button[contains(text(), 'Начать сначала') or contains(text(), 'Решить снова')]")
            reset_btn.click()
            time.sleep(3)
        except:
            pass

        # Ввод
        textarea = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea"))
        )
        textarea.clear()
        answer = math.log(int(time.time()))
        textarea.send_keys(str(answer))
        time.sleep(1)

        # Отправка
        try:
            browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
        except:
            browser.find_element(By.CSS_SELECTOR, "button.attempt-wrapper-button").click()

        # Ждем 5 секунд, чтобы Степик точно успел все отрисовать
        time.sleep(5) 
        
        # Ищем фидбек
        try:
            feedback = browser.find_element(By.CSS_SELECTOR, ".attempt__feedback")
            text = feedback.text.strip()
            
            if text and "Correct" not in text:
                print(f"[+] КУСОЧЕК: '{text}'")
                with open("result.txt", "a", encoding="utf-8") as f:
                    f.write(text + " ")
            else:
                print(f"[-] Текст: '{text}' (наверное, уже решено)")
        except:
            print("[-] Фидбек не найден. Возможно, не засчитан ответ или страница не прогрузилась.")
            # Выведем кусок HTML, чтобы понять, что там
            # print(browser.page_source[:500]) 
            
    except Exception as e:
        print(f"[!] Ошибка: {str(e)[:50]}...")