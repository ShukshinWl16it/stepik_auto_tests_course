from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    # Метод, который вытаскивает название товара
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # Метод, который вытаскивает цену товара
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # Проверяем, что сообщение об успехе вообще появилось
    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    # Проверяем, что название в сообщении совпадает с названием на странице (передаем название как аргумент)
    def should_be_correct_product_name_in_message(self, expected_name):
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert expected_name == message_name, f"Product name mismatch: expected {expected_name}, got {message_name}"

    # Проверяем, что цена в корзине совпадает с ценой на странице (передаем цену как аргумент)
    def should_be_correct_price_in_basket(self, expected_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert expected_price == basket_price, f"Price mismatch: expected {expected_price}, got {basket_price}"