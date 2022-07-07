import time

import pytest
from selenium import webdriver
from PageObject.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.logger.info("********** Testcase 1 Started **********")
        if act_title == "Your store. Login":
            self.driver.save_screenshot(".\\Screenshot\\login.png")
            self.logger.info("********** Testcase 1 Passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("********** Testcase 1 Failed **********")
            assert False

    @pytest.mark.sanity
    def test_Login(self, setup):
        self.logger.info("********** Testcase 2 Started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.l = Login(self.driver)
        self.l.setUserName(self.username)
        time.sleep(2)
        self.l.setPassword(self.password)
        time.sleep(2)
        self.l.clickLogin()
        act_title = self.driver.title
        print(act_title)
        if 'nopCommerce' in act_title:
            self.driver.save_screenshot(".\\Screenshot\\home.png")
            self.logger.info("********** Testcase 2 Passed **********")
            assert True
        else:
            self.logger.error("********** Testcase 2 Failed **********")
            assert False
