from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTests():

    def test_validLogin(self):
        baseURL = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        # Cliclando no botão de Login
        loginLink = driver.find_element(By.XPATH, "//a[@href='/login']")
        loginLink.click()

        # Encontrando e preenchando o campo email
        emailField = driver.find_element(By.ID, "email")
        emailField.send_keys("test@email.com")

        # Encontrando e preenchando o campo senha
        passwordField = driver.find_element(By.ID, "password")
        passwordField.send_keys("abcabc")

        # Apertando o botão de Log in
        loginButton = driver.find_element(By.XPATH, "//input[@value='Login']")
        loginButton.click()

        userIcon = driver.find_element(By.XPATH, "//button[@id='dropdownMenu1']//span[text()='My Account']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login not Successful")


ff = LoginTests()
ff.test_validLogin()

