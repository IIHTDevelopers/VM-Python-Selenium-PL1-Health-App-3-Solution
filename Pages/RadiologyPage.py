import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from datetime import datetime

class RadiologyPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
        self.radiology = {
            "radiology_module": (By.CSS_SELECTOR, 'a[href="#/Radiology"]'),
            "list_request_sub_module": (By.XPATH, '//a[contains(text(),"List Requests")]'),
            "from_date": (By.XPATH, '(//input[@id="date"])[1]'),
            "ok_button": (By.XPATH, '//button[contains(text(),"OK")]'),
            "add_report_button": (By.XPATH, '(//a[contains(text(),"Add Report")])[1]'),
            "close_modal_button": (By.CSS_SELECTOR, 'a[title="Cancel"]')
        }

    def perform_radiology_request_and_handle_alert(self, data):
        """
        /**
        * @Test5
        * @description This method performs a radiology request and handles alerts that may arise during the process.
        *              Navigates through the Radiology module, applies a date filter, attempts to add a report, and handles any resulting alert dialogs.
        *              It loops through the process twice to ensure the requests are handled.
        *
        * @param data: Dictionary containing radiology request parameters, expects a key 'FromDate'
        */
        """
        # try:
        from_date = data.get("FromDate", "")
        print(f"From Date: {from_date}")

        # Loop to repeat the process twice
        for _ in range(2):
            # Step 1: Navigate to Radiology Module and List Request sub-module
            self.driver.find_element(*self.radiology["radiology_module"]).click()
            self.driver.find_element(*self.radiology["list_request_sub_module"]).click()

            # Step 2: Set From Date
            self.driver.find_element(*self.radiology["from_date"]).send_keys(from_date)

            # Step 3: Click OK to apply date filter
            self.driver.find_element(*self.radiology["ok_button"]).click()

            # Step 4: Click "Add Report" button in the table
            self.driver.find_element(*self.radiology["add_report_button"]).click()

            # Step 5: Close the modal
            self.driver.find_element(*self.radiology["close_modal_button"]).click()

            print("is close button still visible ?? $")
            if self.driver.find_element(*self.radiology["close_modal_button"]).is_displayed():
                print("Close button still visible, forcing close.")
                self.driver.find_element(*self.radiology["close_modal_button"]).click()
                # Alternatively, you might press "Enter" if needed:
                # self.closeModalButton.press("Enter")

            time.sleep(2)

            # Press Shift+Tab three times to navigate backward
            for _ in range(3):
                actions = ActionChains(self.driver)
                actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()

            # Press Enter to confirm or close
                actions.send_keys(Keys.ENTER).perform()

            # Step 6: Handle alert
            self.handle_alert()

            self.driver.find_element(*self.radiology["list_request_sub_module"]).click()

        return True

        # except Exception as e:
        #     print(f"Error during radiology request test: {e}")
        #     return False

    def handle_alert(self) -> bool:
        """
        Waits for an alert to appear and handles it.

        If the alert message contains "Changes will be discarded. Do you want to close anyway?",
        the alert is accepted; otherwise, it is dismissed.

        :return: True if the alert was handled, False otherwise.
        """
        try:
            # Wait up to 10 seconds for the alert to be present
            wait = WebDriverWait(self.driver, 10)
            alert = wait.until(EC.alert_is_present())

            # Retrieve the alert's message
            alert_text = alert.text
            print(f"Alert message: {alert_text}")

            # Check for the specific message and handle accordingly
            if "Changes will be discarded. Do you want to close anyway?" in alert_text:
                alert.accept()
                print("Alert accepted.")
            else:
                alert.dismiss()
                print("Alert dismissed.")

            return True

        except Exception as e:
            print(f"Failed to handle alert: {e}")
            return False
