"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriver Factory class
        Returns:
            None
        """
        self.browser = browser
        """
        Set chrome driver and iexplorer enviroment based on OS
        
        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = web.Chrome(chromedriver)
        
        PREFERRED: Set the path on the machine where browser will be executed 
        """

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://courses.letskodeit.com/practice"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefor":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver