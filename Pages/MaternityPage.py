import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MaternityPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.maternity = {
            "maternity_link": (By.XPATH, "//span[text()='Maternity']"),
            "reports_submodule": (By.XPATH, "//a[contains(text(),'Reports')]"),
            "maternity_allowance_report": (By.XPATH, "//i[text()='Maternity Allowance']"),
            "from_date_input": (By.XPATH, '(//input[@id="date"])[1]'),
            "showReport_button": (By.XPATH, "//button[contains(text(),'Show Report')]"),
            "view_details_button": (By.XPATH, "(//a[contains(text(),'View Details')])[1]"),
            "maternity_allowance_receipt_modal": (By.XPATH, "//u[contains(text(),'Maternity Allowance Payment Receipt')]"),
        }

    def verify_maternity_allowance_report(self):
        """
        /**
        * @Test8
        * @description This method verifies the functionality of the Maternity Allowance Report.
        * It navigates to the Maternity module, selects the report, enters the date, and verifies the modal.
        * @expected
        * The "Maternity Allowance Payment Receipt" modal should appear after clicking View Details.
        */
        """
        try:
            # Navigate to the Maternity module
            self.wait.until(EC.element_to_be_clickable(self.maternity["maternity_link"])).click()

            # Navigate to the Reports submodule
            self.wait.until(EC.element_to_be_clickable(self.maternity["reports_submodule"])).click()

            # Select Maternity Allowance Report
            self.wait.until(EC.element_to_be_clickable(self.maternity["maternity_allowance_report"])).click()

            # Enter the From Date
            from_date_input = self.wait.until(EC.visibility_of_element_located(self.maternity["from_date_input"]))
            from_date_input.clear()  # Clear any existing text
            from_date_input.send_keys("01-01-2020")

            # Click the OK button
            self.wait.until(EC.element_to_be_clickable(self.maternity["showReport_button"])).click()

            # Wait for the table to load and click View Details for the first record
            time.sleep(2)  # Adjust this time as necessary for the table to load
            self.wait.until(EC.element_to_be_clickable(self.maternity["view_details_button"])).click()

            # Verify that the "Maternity Allowance Payment Receipt" modal appears
            modal_visible = self.wait.until(EC.visibility_of_element_located(self.maternity["maternity_allowance_receipt_modal"]))
            assert modal_visible.is_displayed(), "Maternity Allowance Payment Receipt modal is not visible."

            print("Maternity Allowance Payment Receipt modal is displayed successfully.")

            return True

        except Exception as e:
            print(f"Test failed due to error: {e}")
            return False