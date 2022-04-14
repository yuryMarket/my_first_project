from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators:
    LOGIN_URL = (By.PARTIAL_LINK_TEXT,"login")
    LOGIN_FORM = (By.CSS_SELECTOR,'#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
        