from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
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
        self.getLoginLink().click()

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    # ===============================================================

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
