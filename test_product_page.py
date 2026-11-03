import pytest
from pages.product_page import ProductPage

@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    
    # 1. Считываем название и цену ДО добавления
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    
    # 2. Добавляем товар и решаем капчу
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    
    # 3. Проверяем сообщение
    page.should_be_add_to_basket_message()
    
    # 4. Проверяем совпадение названия и цены
    page.should_be_correct_product_name_in_message(product_name)
    page.should_be_correct_price_in_basket(product_price)