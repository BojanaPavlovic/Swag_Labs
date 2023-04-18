from confi.config import TestData
from pages.Login_Page import Login_Page
from tests.test_Base import BaseTest

class Test_Login(BaseTest):

    def test_login_page_title(self):
        self.loginPage = Login_Page(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = Login_Page(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)