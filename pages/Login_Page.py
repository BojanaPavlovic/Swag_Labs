"""LIBRARIES"""

from confi.config import TestData
from pages.Base_Page import Base_Page
from selenium.webdriver.common.by import By


class Login_Page(Base_Page):

    """     locators from login page      """

    USERNAME_FIELD     =      (By.ID,       "user-name"   )
    PWD_FIELD          =      (By.ID,       "password"    )
    LOGIN_BUTTON       =      (By.ID,       "login-button")

    """     constructor of the page class      """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    """PAGE ACTIONS FOR LOGIN PAGE"""


    """this is used to login to app"""
    def do_login(self, username, password):
        self.do_send_key (self.USERNAME_FIELD,  username)
        self.do_send_key (self.PWD_FIELD,    password)
        self.do_click    (self.LOGIN_BUTTON)

    """this is used to get page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)
