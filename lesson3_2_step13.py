import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        first_name.send_keys("Ivan")

        last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        last_name.send_keys("Petrov")

        email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        email.send_keys("test@test.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text


        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration failed")
        
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        first_name.send_keys("Ivan")

        last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        last_name.send_keys("Petrov")

        email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        email.send_keys("test@test.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration failed")
        
        browser.quit()

if __name__ == "__main__":
    unittest.main()