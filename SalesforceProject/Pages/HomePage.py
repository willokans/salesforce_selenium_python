from SalesforceProject.Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.app_launcher_class = Locators.app_launcher_class

    def check_app_launcher_isDisplayed(self):
        self.driver.find_element_by_css_selector(self.app_launcher_class).is_displayed()
