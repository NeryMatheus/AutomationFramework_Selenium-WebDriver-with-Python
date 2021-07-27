from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class SeleniumDriver:
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type: " + locatorType + " is not correct/supported !!!")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            print("Element not Found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Clicked on the element with locator: " + locator + " and locatorType: " + locatorType)
        except:
            print("Cannot click on the element with locator: " + locator + " and locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print("Sent data on the element with locator: " + locator + " and locatorType: " + locatorType)
        except:
            print("Cannot sent data on the element with locator: " + locator + " and locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                print("Found element")
                return True
            else:
                print("Elements not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresentCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Elements found")
                return True
            else:
                print("Elements not found")
                return False
        except:
            print("Elements not found")
            return False

    def waitForElement(self, locator, locatorType='xpath', timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.hw.getByType(locatorType)

            print("Waiting for maximum :: " + str(timeout) + " :: seconds for elements to be clickable")

            wait = WebDriverWait(self.driver, 10, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))

            print("Element appeared on the web page")

        except:
            print("Element not appeared on the web page")
            print_stack()

        return element