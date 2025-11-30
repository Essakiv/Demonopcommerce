import pytest
import time
import os

import self
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobject.loginpage import Loginpage
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen
from  Utilities import  XLUtils
class Test_002_DDT_Login:
    baseURL = Readconfig.getApplicationURL()
    path=".//Testdata/logidata.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("*****Test_002_DDT_login****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Loginpage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in a excel:", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(30)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**Passed**")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("**Failed (should not pass)**")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            else:
                if self.exp == "Pass":
                    self.logger.info("**Failed**")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("**Passed (negative test)**")
                    lst_status.append("Pass")

        # --------------------
        # FINAL ASSERT HERE (after loop)
        # --------------------
        if "Fail" not in lst_status:
            self.logger.info("*** Login DDT test passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Login DDT test failed ***")
            self.driver.close()
            assert False
