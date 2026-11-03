from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    
    page = ProductPage(browser, link)
    page.open()
    
    page.add_to_basket()
    
    # Решаем капчу
    page.solve_quiz_and_get_code()
    
    # Делаем проверки 
    page.should_be_add_to_basket_message()
    page.should_product_name_match()
    page.should_product_price_match()