import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from datetime import datetime

class LaboratoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
        self.laboratory = {
            "laboratory_link": (By.CSS_SELECTOR, 'a[href="#/Lab"]'),
            "laboratory_dashboard": (By.CSS_SELECTOR, 'a[href="#/Lab/Dashboard"]'),
            "settings_sub_module": (By.XPATH, '(//a[@href="#/Lab/Settings"])[2]'),
            "add_new_lab_test": (By.XPATH, '//a[contains(text(),"Add New Lab Test")]'),
            "add_button": (By.XPATH, '//button[contains(text(),"Add")]'),
            "close_button": (By.XPATH, '//button[contains(text(),"Close")]'),
            "star_icon": (By.CSS_SELECTOR, 'i[title="Remember this Date"]'),
            "error_message_locator": (
            By.XPATH, '//p[contains(text(),"error")]/../p[contains(text(),"Lab Test Code Required.")]')
        }

    def verify_error_message(self):
        """
        /**
        * @Test4
        * @description This method verifies the error message when attempting to add a new lab test without entering required values.
        *              Navigates to Laboratory > Settings, selects "Add New Lab Test," and clicks the Add button without providing input.
        *              Captures and logs the displayed error message. Note: The "Add Lab Test" modal remains open.
        */
        """
        try:
            error_message_text = ""

            # Navigate to Laboratory > Settings
            self.driver.find_element(self.laboratory["laboratory_link"]).click()

            self.driver.find_element(self.laboratory["settings_sub_module"]).click()

            # Click on Add New Lab Test
            self.driver.find_element(self.laboratory["add_new_lab_test"]).click()

            # Click on Add button without entering any values
            self.driver.find_element(self.laboratory["add_button"]).click()

            # Capture the error message text
            error_locator = self.driver.find_element(self.laboratory["error_message_locator"])
            # Ensure the error message element is visible before capturing its text
            if not error_locator.is_displayed():
                raise Exception("Error message not visible")
            error_message_text = error_locator.text_content() or ""
            print(f"Error message text: {error_message_text}")

            return True

        except Exception as e:
            print(f"Error in verifying error message: {e}")
            return False

    def filter_sample_collections(self):
        """
        /**
        * @Test14
        * @description This method verifies the functionality of filtering sample collections
        * in the Lab Dashboard by entering a date and selecting a specific item.
        * It navigates to the Lab Dashboard, selects the Sample Collections tab,
        * enters the From Date, interacts with the Item column, and applies the filter.
        * @expected
        * The sample collections should be filtered based on the criteria provided.
        */
        """
        try:
            # Click on the Accounting Module
            self.wait.until(EC.element_to_be_clickable(self.laboratory["laboratory_link"])).click()

            # Select the Sample Collections tab
            self.wait.until(EC.element_to_be_clickable(self.laboratory["sample_collections_tab"])).click()

            # Enter the From Date
            from_date_input = self.wait.until(EC.visibility_of_element_located(self.laboratory["from_date_input"]))
            from_date_input.clear()  # Clear any existing text
            from_date_input.send_keys("01-01-2020")

            # Click the OK button
            self.wait.until(EC.element_to_be_clickable(self.laboratory["ok_button"])).click()

            # Wait for the results to load
            time.sleep(2)  # Adjust this time as necessary for the results to load

            # Hover over the Item column
            item_column = self.wait.until(EC.visibility_of_element_located(self.laboratory["item_column"]))
            ActionChains(self.driver).move_to_element(item_column).perform()

            # Click the Hamburger Menu
            self.wait.until(EC.element_to_be_clickable(self.laboratory["hamburger_menu"])).click()

            # Locate the dropdown
            dropdown = self.driver.find_element(By.CSS_SELECTOR, "select#filterType")

            # Create Select object
            select = Select(dropdown)

            # Select by visible text
            select.select_by_visible_text("Starts with")

            # Select "Equals" from the dropdown
            self.wait.until(EC.element_to_be_clickable(self.laboratory["filterOption"])).click()

            # Enter "Male Ward" in the text field
            text_field = self.wait.until(EC.visibility_of_element_located(self.laboratory["filterOption"]))
            text_field.clear()  # Clear any existing text
            text_field.send_keys("Male Ward")

            print("Sample collections filtered successfully for 'Male Ward'.")

            return True

        except Exception as e:
            print(f"Test failed due to error: {e}")
            return False


