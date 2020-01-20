from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from Pages.Locators.item_edition_locator import ItemEditionLocator

"""Problem with time, wait to much"""


class ItemEditionPage():
    def __init__(self, driver):
        self.driver = driver


    def select_item(self):
        originalText = self.driver.find_element_by_css_selector(ItemEditionLocator.pick_an_item_css).text
        self.driver.find_element_by_css_selector(ItemEditionLocator.click_edition_css).click()
        return originalText

    def edit_item(self):
        editionNewText = "Eleven is the new E.T."
        self.driver.find_element_by_xpath(ItemEditionLocator.text_area_path).send_keys(editionNewText)
        updateButton = self.driver.find_element_by_xpath(ItemEditionLocator.button_update_xpath)
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH, ItemEditionLocator.button_update_xpath)))
        updateButton.click()
        wait.until(ec.invisibility_of_element((By.XPATH, ItemEditionLocator.button_update_xpath)))
        return editionNewText

    def verification(self,originalText, editionNewText):
        newText = self.driver.find_element_by_css_selector(ItemEditionLocator.pick_an_item_css ).text

        if originalText + editionNewText == newText:
            print("Succesful Edition")
        else:
            print("Fail")







