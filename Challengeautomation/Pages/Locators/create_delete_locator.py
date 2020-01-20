class CreateDeleteLocators:
    original_list_xpath = "//h1[@class='ng-binding']"
    file_input_xpath = "//input[@id='inputImage']"
    file_location = "//200.png"
    text_area_path = "//textarea[@name='text']"
    button_create_item_xpath = "//button[contains(text(), 'Create Item')]"
    item_added_css = '.ui-sortable-handle:last-child'
    item_adedd_text_css = '.ui-sortable-handle:last-child .story'

    """Delete item locators"""

    find_element_css = '.ui-sortable-handle:last-child button:nth-child(2)'
    delete_confirmation_xpath = '//button[contains(text(), "Yes, delete it!")]'
