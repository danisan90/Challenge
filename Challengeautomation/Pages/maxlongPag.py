from Pages.Locators.max_long_locator import maxLongLocator


class MaxLongPage():
    def __init__(self, driver):
        self.driver = driver

    def enter_description(self, prueba):
        self.driver.find_element_by_xpath(maxLongLocator.text_description_xpath).send_keys(prueba)

    def check_disable_button(self):
        button = self.driver.find_element_by_xpath(maxLongLocator.button_create_xpath)
        disableButton = button.get_property('disabled')
        assert disableButton
