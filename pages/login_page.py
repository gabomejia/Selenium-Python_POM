from .base_actions import BaseActions
from selenium.webdriver.common.by import By

class loginImput:
    userImput = (By.ID, "user-name")
    passwordImput = (By.ID, "password")
    loginButton = (By.ID, "login-button")
    loginError = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    loginSuccess = (By.XPATH, "//div[@class='alert alert-success']")
    loginPageTitle = (By.XPATH, "//h1[contains(text(), 'Login')]")





class LoginActions(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com"
        
    def open_login_page(self):
        self.driver.get(self.url)
        self.locators = loginImput()
    
    def enter_username(self, username):
        self.send_keys(self.locators.userImput, username)

    def enter_password(self, password):
        self.send_keys(self.locators.passwordImput, password)
    
    def click_login_button(self):
        self.click(self.locators.loginButton)
    
    def get_login_error(self):
        return self.get_text(self.locators.loginError)
        print("Login error message:", error_message)
    
    def get_login_success(self):
        return self.get_text(self.locators.loginSuccess)

    