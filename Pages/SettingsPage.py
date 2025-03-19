from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        self.settings = {
            "settings_link": (By.CSS_SELECTOR, 'a[href="#/Settings"]'),
            "more_dropdown": (By.XPATH, '//a[contains(text(),"More...")]'),
            "price_category_tab": (By.CSS_SELECTOR, 'ul.dropdown-menu a[href="#/Settings/PriceCategory"]'),
            "activate_success_message": (By.XPATH, '//p[contains(text(),"success")]/../p[text()="Activated."]'),
            "deactivate_success_message": (By.XPATH, '//p[contains(text(),"success")]/../p[text()="Deactivated."]'),
        }

    def verify_occupied_bed_edit(self):
        """
        /**
        * @Test9
        * @description This method verifies that an error message is displayed when attempting to edit an occupied bed.
        * @expected
        * An error message should appear stating: "Cannot modify occupied beds."
        */
        """
        try:
            # Navigate to Settings Module
            self.wait.until(EC.element_to_be_clickable(self.settings["settings_link"])).click()

            # Navigate to Manage Bed tab
            self.wait.until(EC.element_to_be_clickable(self.settings["adt_Link"])).click()

            # Navigate to Manage Bed tab
            self.wait.until(EC.element_to_be_clickable(self.settings["manage_bed_tab"])).click()

            # Click on the Edit button for an occupied bed
            self.wait.until(EC.element_to_be_clickable(self.settings["occupied_bed_edit_button"])).click()

            # Wait for the error message to appear
            error_message = self.wait.until(EC.visibility_of_element_located(self.settings["error_message"]))

            # Verify the error message
            assert error_message.is_displayed(), "Error message is not displayed."
            assert error_message.text.strip() == "Cannot modify occupied beds.", f"Expected error message not found. Found: {error_message.text.strip()}"

            print("Error message displayed successfully: 'Cannot modify occupied beds.'")

            return True

        except Exception as e:
            print(f"Test failed due to error: {e}")

            return False