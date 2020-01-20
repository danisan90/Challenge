from selenium import webdriver
from Pages.finditemPage import FindItemPage
import unittest


class FindItem(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="/home/danisan/Documents/drivers/chromedriver")
        self.driver.get('http://immense-hollows-74271.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_find_item_ok(self):
        driver =self.driver
        item_scan = FindItemPage(driver)
        item_scan.scan_items()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

