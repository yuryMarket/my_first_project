import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks = pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_name()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()    
    page.should_be_only_test_product_in_basket()
    page.should_product_in_basket_be_test_product()

@pytest.mark.xfail        
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_is_dissapeared()   
       
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link() 

@pytest.mark.need_review     
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review     
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_from_main_page()
    page.should_be_no_product_in_basket()
    page.should_be_message_about_no_product_in_basket()     

class TestUserAddToBasketFromProductPage: 
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email= str(time.time()) + "@fakemail.org"
        password=str(time.time())+'12345'     
        link = 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email,password)
        page.should_be_authorized_user()
        
    @pytest.mark.xfail     
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()
    
    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_name()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()    
        page.should_be_only_test_product_in_basket()
        page.should_product_in_basket_be_test_product() 
            
    
              