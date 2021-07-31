from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTests(unittest.TestCase):
    baseURL = 'https://courses.letskodeit.com/practice'
    driver = webdriver.Firefox()
    driver.maximize_window()
    login_Page = LoginPage(driver)
    driver.implicitly_wait(3)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.login_Page.login("test@email.com", "abcabc")

        result = self.login_Page.verifyLoginSuccessful()
        assert result == True

        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.login_Page.login("test@email.com", "abcabc091022091022091022091022")

        result = self.login_Page.verifyLoginFailed()
        assert result == True
