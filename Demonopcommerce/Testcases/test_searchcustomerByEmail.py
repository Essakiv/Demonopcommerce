import pytest
import time
import string
import random

from pageobject.loginpage import loginpage
from pageobject.test_addcustomer import AddCustomerpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

from pageobject.searchcustomer import SearchCustomer


class Test_004_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************** Test_003_AddCustomer **********")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***** Login successful *****")

        # Add Customer Page
        self.addcust = AddCustomer(self.driver)

        self.logger.info("***** Starting Add Customer Test *****")
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.logger.info("***** searching customer by emailid *****")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoia@opcommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoia@opcommerce.com")
        assert True==status
        self.logger.info("****tc_searchcustomer_by_email_004 finished")
        self.driver.close()
