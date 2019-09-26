from selenium import webdriver
import os
import unittest
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from SalesforceProject.Pages.LoginPage import LoginPage
from SalesforceProject.Pages.HomePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="/Users/Will/Desktop/Workspace/Python/SalesfroceDev/SalesforceProject/Drivers/Firefox/geckodriver")
        cls.driver.implicitly_wait(10)
        # driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        homepage = HomePage(driver)

        driver.get("https://login.salesforce.com/?locale=eu")

        login.enter_username("willdev_01@dev01.com")
        login.enter_password(os.environ['password'])
        login.click_login()
        homepage.check_app_launcher_isDisplayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()







