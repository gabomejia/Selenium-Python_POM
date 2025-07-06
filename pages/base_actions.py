from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BaseActions:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    def is_displayed(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()
    

    def wait_for_element(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Element {locator} not found within {timeout} seconds.")
            return None
        return self.driver.find_element(*locator)
    

