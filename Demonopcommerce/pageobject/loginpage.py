from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Loginpage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(@class,'login-button')]"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds wait

    def setUserName(self, username):
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, self.textbox_username_id)))
        username_field.clear()
        username_field.send_keys(username)

    def setPassword(self, password):
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, self.textbox_password_id)))
        password_field.clear()
        password_field.send_keys(password)

    def clickLogin(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
        login_button.click()

    def clickLogout(self):
        logout_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.link_logout_linktext)))
        logout_link.click()
