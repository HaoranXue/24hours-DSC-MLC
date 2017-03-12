import tensorflow as tf
import sklearn as sk
import os,sys,time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import re
import random
from PIL import Image
import os


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/VC/Documents/chromedriver')
        self.driver.maximize_window()

    def test_Login(self):
        waitTime = 10

        url = 'https://www.bloomberg.com/press-releases/2016-12-20/abm-industries-announces-departure-of-sarah-hlavinka-mcconnell-executive-vice-president-general-counsel-and-corporate-secret'
        self.driver.get(url)
        driver = self.driver



        # sendPath = ".//*[@id='kw']"
        # sendElement = WebDriverWait(driver, waitTime).until(lambda driver: driver.find_element_by_xpath(sendPath))
        # sendElement.send_keys("hello world")
        # sendElement.send_keys("oh crap")
        # WebDriverWait(driver, waitTime).until(lambda driver: driver.find_element_by_xpath(".//*[@id='su']")).click()
        # Y = 500
        # driver.execute_script("window.scrollTo(0, " + str(Y) + ")")
        #
        time.sleep(10)
        print(driver.page_source)
        # WebDriverWait(driver, waitTime).until(lambda driver: driver.find_element_by_xpath(".//*[@id='1']/h3/a")).click()
        time.sleep(10)
        # driver.page_source
        #
        # # WebDriverWait(driver, waitTime).until(lambda driver: driver.find_element_by_xpath(Xpath)).click()
        # # page2Element = WebDriverWait(driver, waitTime).until(lambda driver: driver.find_element_by_xpath(page2Path))
        # # page2Element.send_keys(str(i))


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

