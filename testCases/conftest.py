
import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(1)
    driver.get("https://admin-demo.nopcommerce.com/")
    return driver