from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

class ProcurementPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.procurement = {
            "procurement_link": (By.CSS_SELECTOR, 'a[href="#/ProcurementMain"]'),
            "purchase_request": (By.XPATH, '//a[contains(text(),"Purchase Request")]'),
            "purchase_order": (By.XPATH, '(//a[contains(text(),"Purchase Order")])[1]'),
            "goods_arrival_notification": (By.XPATH, '//a[contains(text(),"Goods Arrival Notification")]'),
            "quotations": (By.XPATH, '//a[contains(text(),"Quotation")]'),
            "settings": (By.XPATH, '//a[contains(text(),"Settings")]'),
            "reports": (By.XPATH, '//a[contains(text(),"Reports")]'),
            "favorite_button": (By.XPATH, '//i[contains(@class,"icon-favourite")]'),
            "ok_button": (By.XPATH, '//button[contains(text(),"OK")]'),
            "print_button": (By.XPATH, '//button[text()="Print"]'),
            "first_button": (By.XPATH, '//button[text()="First"]'),
            "previous_button": (By.XPATH, '//button[text()="Previous"]'),
            "next_button": (By.XPATH, '//button[text()="Next"]'),
            "last_button": (By.XPATH, '//button[text()="Last"]'),
            "from_date": (By.XPATH, '(//input[@id="date"])[1]'),
            "to_date": (By.XPATH, '(//input[@id="date"])[2]'),
            "invalid_msg": (By.XPATH, '//div[contains(@class,"invalid-msg-cal")]'),
            "requested_date_column": (By.CSS_SELECTOR, 'div[col-id="RequestDate"]')
        }

    def verify_purchase_request_list_elements(self):
        """
        /**
        * @Test3
        * @description This method navigates to the Procurement module and verifies the visibility of various purchase request list elements.
        */
        """
        try:
            # Navigate to Procurement module
            self.driver.find_element(*self.procurement["procurement_link"]).click()
            time.sleep(2)

            # Define the list of elements to verify visibility
            elements = [
                self.procurement["purchase_request"],
                self.procurement["purchase_order"],
                self.procurement["goods_arrival_notification"],
                self.procurement["quotations"],
                self.procurement["settings"],
                self.procurement["reports"],
                self.procurement["favorite_button"],
                self.procurement["ok_button"],
                self.procurement["print_button"],
                self.procurement["first_button"],
                self.procurement["previous_button"],
                self.procurement["next_button"],
                self.procurement["last_button"],
            ]

            # Highlight the fromDate element and type the date "01-01-2020" with a delay of 100ms
            self.driver.find_element(*self.procurement["from_date"]).send_keys("01-01-2020")

            # Highlight and click the OK button
            self.driver.find_element(*self.procurement["ok_button"]).click()

            # Loop through each element to verify its visibility
            for element in elements:
                if not self.driver.find_element(*element).is_displayed():
                    print("Element not found on page:", self.driver.find_element(*element).text)
                    raise Exception("Element not found on the page")

            return True

        except Exception as e:
            print(f"Error in verifying Purchase Request List Elements: {e}")
            return False

    def verify_notice_message_after_entering_incorrect_filters(self):
        """
        /**
        * @Test7
        * @description This method verifies the error message displayed after entering an invalid date in the filter.
        *              Navigates to the Procurement module, selects the Purchase Request tab, and applies an invalid date filter.
        *              Captures and validates the error message to confirm that the application correctly identifies the invalid input.
        */
        """
        try:
            actual_error_message = ""
            self.driver.find_element(*self.procurement["procurement_link"]).click()

            self.driver.find_element(*self.procurement["purchase_request"]).click()

            self.driver.find_element(*self.procurement["from_date"]).send_keys("00-00-0000")

            self.driver.find_element(*self.procurement["ok_button"]).click()

            actual_error_message = self.driver.find_element(*self.procurement["invalid_msg"]).text
            print(
                f"----------------------------Invalid Error Message --->> {actual_error_message}----------------------------")

            if actual_error_message.strip() != "Date is not between Range. Please enter again":
                print("Error: Unexpected error message.")
                return False

            return True

        except Exception as e:
            print(f"Error in verifying notice message after entering incorrect filters: {e}")
            return False
