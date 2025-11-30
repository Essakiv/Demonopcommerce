import pytest
import time
import string
import random

from pageobject.loginpage import loginpage
from pageobject.test_addcustomer import AddCustomerpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
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
        self.addcust.clickOnAddnew()

        self.logger.info("***** Providing customer info *****")

        email = random_generator() + "@gmail.com"
        self.addcust.setEmail(email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Sakthi")
        self.addcust.setLastName("Vel")
        self.addcust.setDob("5/05/1997")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("Testing Purpose")
        self.addcust.clickOnSave()

        self.logger.info("***** Saving customer info *****")

        # Validation
        self.logger.info("***** Verifying expected message *****")
        self.msg = self.driver.find_element("xpath", "//div[@class='alert alert-success alert-dismissable']").text

        print(self.msg)

        if 'customer has been added successfully.' in self.msg.lower():
            self.logger.info("*** Add customer Test Passed ***")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("*** Add customer Test Failed ***")
            assert False

        self.driver.close()
        self.logger.info("*** Ending Add Customer Test ***")


# ---------------------------
# Random Email Generator
# ---------------------------
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
