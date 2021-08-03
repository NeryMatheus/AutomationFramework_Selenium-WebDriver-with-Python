from selenium.webdriver.common.by import By

from traceback import print_stack

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver:

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("#### EXCEPTION OCCURRED")
            print_stack()

    def getTitle(self):
        return self.driver.title

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
            self.log.info("Locator type: " + locatorType + " is not correct/supported !!!")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element not Found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on the element with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " and locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on the element with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Cannot sent data on the element with locator: " + locator + " and locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Found element")
                return True
            else:
                self.log.info("Elements not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresentCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Elements found")
                return True
            else:
                self.log.info("Elements not found")
                return False
        except:
            self.log.info("Elements not found")
            return False

    def waitForElement(self, locator, locatorType='xpath', timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.hw.getByType(locatorType)

            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for elements to be clickable")

            wait = WebDriverWait(self.driver, 10, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))

            self.log.info("Element appeared on the web page")

        except:
            self.log.info("Element not appeared on the web page")
            print_stack()

        return element