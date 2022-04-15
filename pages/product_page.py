from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
import time
import math


class ProductPage(BasePage):
    product_name = None
    def add_product_to_basket(self):
        self.should_be_basket_button()
        self.go_to_basket()       
        
    def should_be_product_name(self):
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON)
    def go_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()        
    def should_be_only_test_product_in_basket(self):    
        total_basket = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)#.text
        text_basket_total = total_basket.text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert text_basket_total==product_price, 'There is not only test product in basket'
    def should_product_in_basket_be_test_product(self):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert self.product_name == product_name_in_basket, 'Product in basket not the test product'
                
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        
    # def should_be_added_product_in_basket(self):
    #     basket_message = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE)
    #     assert self.is_element_present(*ProductPageLocators.BASKET_MESSAGE), 'There is no message on basket page'   
    #     assert ProductPageLocators.PRODUCT_NAME in basket_message, 'There is another product in basket'
    

                
        
        
            
       
           
