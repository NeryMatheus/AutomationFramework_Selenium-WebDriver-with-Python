from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _loginLink = "//a[@href='/login']"
    _emailField = "email"
    _passwordField = "password"
    _loginButton = "//input[@value='Login']"

    def getLoginLink(self):
        return self.driver.find_element(By.XPATH, self._loginLink)

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._emailField)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._passwordField)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._loginButton)

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

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
