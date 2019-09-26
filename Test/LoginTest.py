from selenium import webdriver
import time
import os

driver = webdriver.Firefox(executable_path="/Users/Will/Desktop/Workspace/Python/SalesfroceDev/Test/Drivers/Firefox/geckodriver")
# driver = webdriver.Chrome()


driver.set_page_load_timeout(10)
# driver.implicitly_wait(4)

driver.get("https://login.salesforce.com/?locale=eu")

driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("willdev_01@dev01.com")

driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys(os.environ['password'])

driver.find_element_by_id("Login").click()
driver.find_element_by_link_text("Remind Me Later")
driver.refresh()
time.sleep(5)
driver.quit()