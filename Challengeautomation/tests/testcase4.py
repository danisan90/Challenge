from selenium import webdriver
from Pages.maxlongPag import MaxLongPage
from Pages.utils import Utils
import unittest


class MaxLongInputTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="/home/danisan/Documents/drivers/chromedriver")
        self.driver.get('http://immense-hollows-74271.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def test_max_long_ok(self):
        """1- In the section “Item Details” select the text area and write a text with more than 300
        characters. E.g ​ https://www.blindtextgenerator.com/lorem-ipsum"""
        driver = self.driver

        max_long = MaxLongPage(driver)
        max_long.enter_description(Utils.randomString(301))
        max_long.check_disable_button()
        print("Successful Test")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
