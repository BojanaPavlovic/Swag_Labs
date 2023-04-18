from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#          DOCUMENTATION
"""THIS CLASS IS THE PARENT OF ALL PAGES"""
"""IT CONTAINS ALL THE GENERIC METHODS AND UTILITIES FOR THE ALL PAGES"""

class Base_Page:

    def __init__(self, driver):
        self.driver = driver


    def do_click(self, by_locator):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        element.click()


    def do_send_key(self, by_locator, text):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)


    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        return element.text


    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        return bool(element)


    def get_title(self, title):
        WebDriverWait(self.driver,20).until(EC.title_is(title))
        return self.driver.title


    def scroll_to_the_element(self, by_locator):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()


    def get_link(self, by_locator):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        return element.get_attributr("href")


