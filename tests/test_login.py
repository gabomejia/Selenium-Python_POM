from selenium import webdriver
from pages.login_page import LoginActions

import pytest

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_login_success(driver):
    login_actions = LoginActions(driver)
    login_actions.open_login_page()
    login_actions.enter_username("standard_user")
    login_actions.enter_password("secret_sauce")
    login_actions.click_login_button()

def test_login_error(driver):
    login_actions = LoginActions(driver)
    login_actions.open_login_page()
    login_actions.enter_username("standard_user")
    login_actions.enter_password("test")
    login_actions.click_login_button()
    error_message = login_actions.get_login_error()
    print("Login error message:", error_message)
    assert "Epic sadface: Username and password do not match any user in this service" in error_message, "Login error message did not match expected text."
    

