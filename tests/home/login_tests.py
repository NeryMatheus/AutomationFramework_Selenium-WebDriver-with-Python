from pages.home.login_page import LoginPage
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.login_Page = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.login_Page.login("test@email.com", "abcabc")
        result1 = self.login_Page.verifyTitle()
        assert result1 == True
        result2 = self.login_Page.verifyLoginSuccessful()
        assert result2 == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.login_Page.login("test@email.com", "abcabc091022091022091022091022")
        time.sleep(2)
        result = self.login_Page.verifyLoginFailed()
        assert result == True
