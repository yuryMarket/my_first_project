
from .pages.product_page import ProductPage
import time
from .pages.locators import ProductPageLocators



def test_get_code(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_name()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()    
    page.should_be_only_test_product_in_basket()
    page.should_product_in_basket_be_test_product()
    #time.sleep(3000)
    
    #assert product_in_basket
    #assert basket_sum = product_price