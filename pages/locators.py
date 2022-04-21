from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    

class BasketPageLocators:
    PRODUCT = (By.CSS_SELECTOR,'.product_main h1')
    MESSAGE_NO_PRODUCT = (By.CSS_SELECTOR,'#content_inner > p')       
    
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR,'#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_SUBMIT = (By.CSS_SELECTOR, '#register_form > button')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
        
class ProductPageLocators:
    BASKET_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ' .alertinner')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")
    PRODUCT_NAME = (By.CSS_SELECTOR,'.product_main h1')    
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR,'#messages .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong')
    
    
     
        
    