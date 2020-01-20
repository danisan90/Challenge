from selenium import webdriver
from Pages.createitemPage import CreateItemPage
from Pages.deleteitemPage import DeleteItemPage

import unittest


class CreateDeleteItemTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/danisan/Documents/drivers/chromedriver")
        self.driver.get('http://immense-hollows-74271.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_create_item(self):
        """1- In the section “Item Details”, click on “Choose file”
        2- Select an image
        3- Fill the text area with a text (max 300 characters), e.g “New Text”.
        4- Select button “Create Item”"""
        driver = self.driver
        item_new = CreateItemPage(driver)

        item_new.item_image()
        item_new.item_description(item_new.item_image())
        item_new.item_creation()
        item_new.check_new_item(item_new.item_image())
        self.item_new = item_new
        """1- Select the item previously created, click on “Delete”.
        2- Click in “Yes, delete it!”"""

        item_delete = DeleteItemPage(driver)
        item_delete.select_item()
        item_delete.check_item_deleted(self.item_new.item_image())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
