from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url ,'Current url is not login url'
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),'Login form is not present'
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),'Register form is not present'
    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        reg_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)   
        reg_confirm_password = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD)
        reg_email.send_keys(email)
        reg_password.send_keys(password)
        reg_confirm_password.send_keys(password)
        submit_reg = self.browser.find_element(*LoginPageLocators.REG_SUBMIT)
        submit_reg.click()
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"    