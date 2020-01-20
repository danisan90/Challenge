from Pages.Locators.find_item_locator import FindItemLocator
class FindItemPage():
    def __init__(self, driver):
        self.driver = driver


    def scan_items(self):
        listOfItems = self.driver.find_elements_by_css_selector(FindItemLocator.list_description)

        for item in listOfItems:
            if 'Creators: Matt Duffer, Ross Duffer' in item.text:
                print("Item found: " + item.text)
                break

