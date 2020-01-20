from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from Pages.Locators.create_delete_locator import CreateDeleteLocators


class DeleteItemPage():
    def __init__(self, driver):
        self.driver = driver

    def select_item(self):
        self.driver.find_element_by_css_selector(CreateDeleteLocators.find_element_css).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, CreateDeleteLocators.delete_confirmation_xpath))).click()

    def check_item_deleted(self, newText):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            ec.invisibility_of_element((By.XPATH, "//ul/li/div/div[1]/div[2]/p[contains(text(), '" + newText + "')])")))
        print("Item deleted")
