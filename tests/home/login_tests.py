from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = 'https://courses.letskodeit.com/practice'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        login_Page = LoginPage(driver)
        login_Page.login("test@email.com", "abcabc")

        userIcon = driver.find_element(By.XPATH, "//button[@id='dropdownMenu1']//span[text()='My Account']")
        if userIcon is not None:
            print("Login Successful")
            driver.quit()
        else:
            print("Login not Successful")
            driver.quit()