import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager


@pytest.fixture(params=["chrome"], scope = 'class')
def init_driver(request):

    """CHROME BROWSER"""
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())

    """CHROME BROWSER"""
    if request.param == "edge":
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    """OPERA BROWSER"""
    if request.param == "opera":
        web_driver = webdriver.Opera(executable_path = OperaDriverManager().install())

    """FIREFOX BROWSER"""
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path = GeckoDriverManager.install())

    request.cls.driver = web_driver
    yield
    web_driver.close()