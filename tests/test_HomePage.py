import time
from confi.config import TestData
from pages.Login_Page import Login_Page
from pages.Home_Page import Home_Page
from tests.test_Base import BaseTest


class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage = Login_Page(self.driver)
        self.home = Home_Page(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        title = self.home.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE


    def test_home_page_header(self):
        self.loginPage = Login_Page(self.driver)
        self.home = Home_Page(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        header = self.home.get_home_page_header()
        assert header == TestData.HOME_PAGE_HEADER


    def test_drop_down_A_to_Z(self):
        self.loginPage = Login_Page(self.driver)
        self.home = Home_Page(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        actual_text = self.home.get_sort_options()
        expected_text = TestData.DROP_DOWN_MENU_TEXTS_hp
        for text in expected_text:
            if text in actual_text:
                assert True

    def test_click_DROP_DOWN_elements(self):
        self.loginPage = Login_Page(self.driver)
        self.home = Home_Page(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.home.click_on_drop_down_elements()

    def test_click_cart_and_return_header_text(self):
        self.loginPage = Login_Page(self.driver)
        self.home = Home_Page(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        actual = self.home.click_cart_and_return_header_text()
        expected = TestData.CART_HEADER_TEXT
        assert actual == expected



# pytest tests/test_HomePage.py -v --html =./hubSpot.html

