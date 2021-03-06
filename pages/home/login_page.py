from base.basepage import BasePage

import utilities.custom_logger as cl
import logging


class LoginPage(BasePage):
    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _loginLink = "//a[@href='/login']"
    _emailField = "email"
    _passwordField = "password"
    _loginButton = "//input[@value='Login']"

    # ================================================================================

    def clickLoginLink(self):
        self.elementClick(self._loginLink, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._emailField)

    def enterPassword(self, password):
        self.sendKeys(password, self._passwordField)

    def clickLoginButton(self):
        self.elementClick(self._loginButton, locatorType="xpath")

    # ===============================================================

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//button[@id='dropdownMenu1']//span[text()='My Account']", "xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(), 'Your username or password is invalid. Please try again"
                                       ".')]", "xpath")
        return result

    def verifyTitle(self):
        return self.verifyTitlePage("Google")
