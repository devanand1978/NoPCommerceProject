import logging
import time

import pytest
from selenium import webdriver
from PageObject.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import excelUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self, setup):
        self.logger.info("********** Testcase 2 Started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.l = Login(self.driver)
        self.rows = excelUtils.getRowCount(self.path, 'Sheet1')
        status = []
        for r in range(2, self.rows + 1):
            self.user = excelUtils.readData(self.path, 'Sheet1', r, 1).strip()
            self.password = excelUtils.readData(self.path, 'Sheet1', r, 2).strip()
            self.exp = excelUtils.readData(self.path, 'Sheet1', r, 3).strip()
            self.l.setUserName(self.user)
            self.l.setPassword(self.password)
            self.l.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** PASSED ****")
                    # self.l.clickLogout()
                    time.sleep(5)
                    status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**** Failed ****")
                    # self.l.clickLogout()
                    time.sleep(5)
                    status.append("Fail")
            if act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Failed ****")
                    # self.l.clickLogout()
                    time.sleep(5)
                    status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**** Passed ****")
                    # self.l.clickLogout()
                    time.sleep(5)
                    status.append("Pass")
        if "Fail" not in status:
            self.logger.info("*** Finally DDT Testcase Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Finally DDT Testcase Failed ***")
            self.driver.close()
            assert False

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
