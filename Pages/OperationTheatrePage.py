from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OperationTheatrePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.ot_booking = {
            "operation_theatre_link": (By.CSS_SELECTOR, 'a[href="#/OperationTheatre"]'),
            "new_ot_booking_button": (By.XPATH, '//button[contains(text(),"New OT Booking")]'),
            "add_new_ot_button": (By.CSS_SELECTOR, 'input[value="Add New OT"]'),
            "modal_heading": (By.CSS_SELECTOR, 'div.modelbox-div'),
        }

    def verify_ot_booking(self):
        """
        /**
        * @Test11
        * @description This method verifies the functionality of the OT Booking process.
        * It navigates to the OT Booking List, clicks the new OT booking button,
        * and verifies the Remarks text area is enabled and its placeholder.
        * @expected
        * The Remarks text area should be enabled and have the correct placeholder text.
        */
        """
        try:
           # Click on the Operation Theatre Module
            self.wait.until(EC.element_to_be_clickable(self.ot_booking["operation_theatre_link"])).click()

            # Click on the New OT Booking button
            self.wait.until(EC.element_to_be_clickable(self.ot_booking["new_ot_booking_button"])).click()

            # Verify Remarks Text area is enabled
            remarks_text_area = self.wait.until(EC.visibility_of_element_located(self.ot_booking["remarks_text_area"]))
            assert remarks_text_area.is_enabled(), "Remarks text area is not enabled."

            # Verify the placeholder name of Remarks text area
            expected_placeholder = "Remarks"  # Adjust this to the expected placeholder text
            actual_placeholder = remarks_text_area.get_attribute("placeholder")
            assert actual_placeholder == expected_placeholder, f"Expected placeholder '{expected_placeholder}', but got '{actual_placeholder}'."

            print("OT Booking Remarks text area is enabled and placeholder is correct.")

            return True

        except Exception as e:
            print(f"Test failed due to error: {e}")
            return False