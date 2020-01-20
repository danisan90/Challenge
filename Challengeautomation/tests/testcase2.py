from selenium import webdriver
import unittest
import sys
sys.path.insert(0, "/home/Challenges/challengeautomation/Pages")
from Pages.itemeditionPag import ItemEditionPage


class ItemEditionTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="/home/danisan/Documents/drivers/chromedriver")
        self.driver.get('http://immense-hollows-74271.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_item_edition_ok(self):
        """1- Select an item of the list
            2- Click button “Edit” ---Expected Result:The Items Details must have the information of the
            item---
            3- Click on “Choose File” and select a new image.
            4- Add text in the text area.
            5-Click in button Update Item"""
        driver = self.driver

        item_edition = ItemEditionPage(driver)
        item_edition.select_item()
        item_edition.edit_item()
        item_edition.verification(item_edition.select_item(), item_edition.edit_item())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
