from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from Pages.Locators.create_delete_locator import CreateDeleteLocators

class CreateItemPage():
    def __init__(self, driver):
        self.driver = driver


    def item_image(self):
        newText = "Billy escapes from the mill after being subdued by the creature, having a vision of Upside Down where a doppelgänger instructs him to 'buildit'"
        """originalList = self.driver.find_element_by_xpath(self.file_input_xpath).text"""
        file_input = self.driver.find_element_by_xpath(CreateDeleteLocators.file_input_xpath)
        file_input.send_keys(CreateDeleteLocators.file_location)
        return newText

    def item_description(self,newText):
        self.driver.find_element_by_xpath(CreateDeleteLocators.text_area_path).send_keys(newText)

    def item_creation(self):
        self.driver.find_element_by_xpath(CreateDeleteLocators.button_create_item_xpath).click()

    def check_new_item(self, newText):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, CreateDeleteLocators.item_added_css), newText))
        newElement = self.driver.find_element_by_css_selector(CreateDeleteLocators.item_adedd_text_css).text
        assert newElement == newText
        print("Succesful Creation")









