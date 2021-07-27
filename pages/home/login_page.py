from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # Cliclando no botão de Login
        loginLink = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        loginLink.click()

        # Encontrando e preenchando o campo email
        emailField = self.driver.find_element(By.ID, "email")
        emailField.send_keys(username)

        # Encontrando e preenchando o campo senha
        passwordField = self.driver.find_element(By.ID, "password")
        passwordField.send_keys(password)

        # Apertando o botão de Log in
        loginButton = self.driver.find_element(By.XPATH, "//input[@value='Login']")
        loginButton.click()