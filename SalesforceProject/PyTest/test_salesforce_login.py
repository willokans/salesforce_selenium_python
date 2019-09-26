from selenium import webdriver
import os
import time
import pytest

class TestSample():
    @pytest.fixture()
    def test_set(self):
        global driver
        driver = webdriver.Firefox(executable_path="/Users/Will/Desktop/Workspace/Python/SalesfroceDev/SalesforceProject/Drivers/Firefox/geckodriver")
        driver.implicitly_wait(10)

        yield
        driver.close()
        # driver.quit()
        print("Test completed!")

    def test_login(self, test_set):
        driver.get("https://login.salesforce.com/?locale=eu")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("willdev_01@dev01.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("Auto2019")
        driver.find_element_by_id("Login").click()
        # time.sleep(15)
        driver.find_element_by_xpath("//a[text()='Remind Me Later']").click()


    # def test_teadown():
    #     driver.close()
    #     # driver.quit()
    #     print("Test completed!")








