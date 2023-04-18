"""LIBRARIES"""
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from pages.Base_Page import Base_Page
from selenium.webdriver.common.by import By

class Home_Page(Base_Page):

    """locator for the Home Page :) """

    HEADER_HOME_PAGE             =          ( By.CLASS_NAME  ,"app_logo"                                   )
    SORT_DROPDOWN                =          ( By.XPATH       , "//select[@class='product_sort_container']" )
    CART                         =          ( By.CLASS_NAME  , "shopping_cart_link"                        )
    CART_HEADER                  =          ( By.CLASS_NAME  , "title"                                     )
    A_to_Z                       =          (By.CLASS_NAME   , "product_sort_container"                    )
    VALUES                       =          ["az","za"]
    """Constructor """

    def __init__(self, driver):
        super().__init__(driver)

    """ All Home-Page Methods """

    def get_home_page_header(self):
        return self.get_element_text(self.HEADER_HOME_PAGE)

    def get_sort_options(self):
        sort_dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        select = Select(sort_dropdown)
        options = select.options
        option_texts = [option.text for option in options]
        return option_texts

    def click_on_drop_down_elements(self):
        sort_dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        select = Select(sort_dropdown)
        for value in self.VALUES:
            time.sleep(4)
            select.select_by_value(value)

    def click_cart_and_return_header_text(self):
        if self.is_visible(self.CART):
            self.do_click(self.CART)
            try:
                header_text = self.get_element_text(self.CART_HEADER)
                return header_text
            except TimeoutException:
                print("Timed out waiting for cart header text to appear.")
        return None
