import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobject.loginpage import Loginpage
from Utilities.readproperties import Readconfig
from Utilities.customlogger import LogGen


class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def save_screenshot(self, name):
        screenshots_dir = "Screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        self.driver.save_screenshot(os.path.join(screenshots_dir, name))

    def test_homepageTitle(self, setup):
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("***** Verifying home page title *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        exp_title = "nopCommerce demo store. Login"

        if act_title != exp_title:
            self.save_screenshot("homepage_title_failed.png")
            self.logger.error("***** Home page title FAILED *****")
        else:
            self.logger.info("***** Home page title PASSED *****")

        assert act_title == exp_title

    def test_login(self, setup):
        self.logger.info("******* Verifying Login Test *******")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Dashboard")
        )

        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"

        if act_title != exp_title:
            self.save_screenshot("login_failed.png")
            self.logger.error("******* Login test FAILED *******")
        else:
            self.logger.info("******* Login test PASSED *******")

        assert act_title == exp_title
