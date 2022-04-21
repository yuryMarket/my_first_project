from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):    
    def should_be_no_product_in_basket(self):
        self.is_not_element_present(*BasketPageLocators.PRODUCT)
            
    def should_be_message_about_no_product_in_basket(self):
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_NO_PRODUCT)
        basket_text = message.text
        print(basket_text)
        assert basket_text == 'Your basket is empty. Continue shopping', 'Basket is not empty'