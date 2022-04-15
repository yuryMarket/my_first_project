from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR,'#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
        
class ProductPageLocators:
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR,'.product_main h1')    
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR,'#messages .alertinner strong')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_MESSAGE = (By.CSS_SELECTOR, ' .alertinner') 
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")    