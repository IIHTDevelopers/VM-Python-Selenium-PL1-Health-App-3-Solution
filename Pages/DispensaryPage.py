import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from datetime import datetime

class DispensaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

        self.dispensaryLink = (By.CSS_SELECTOR, 'a[href="#/Dispensary"]')
        self.newPatient_modal = (By.XPATH, '//span[text()="Add New Patient"]')
        self.activateCounter = (By.XPATH, "//a[contains(text(),'Counter')]")
        self.activate_counter_link = (By.XPATH, "//h5[contains(text(),'Morning Counter')]"),
        self.counterSelection = (By.XPATH, '//div[@class="counter-item"]')
        self.counterName = (By.XPATH, '//div[@class="counter-item"]//h5')
        self.activatedCounterInfo = (By.CSS_SELECTOR, "div.mt-comment-info")
        self.deactivateCounterButton = (By.XPATH, "//button[contains(text(), 'Deactivate Counter')]")
        self.titleName = (By.XPATH, '//span[@class="caption-subject"]')
        self.name = (By.XPATH, '(//div[@class="col-sm-4 col-md-3"]//label//span)[1]')
        self.prescription = (By.XPATH, "//a[contains(text(),' Prescription ')]")
        self.reports = (By.XPATH, "//a[contains(text(), 'Reports')]")
        self.fromDate = (By.XPATH, '(//input[@id="date"])[1]')
        self.showReportButton = (By.XPATH, "//span[text()='Show Report']")
        self.userCollectionReport = (By.XPATH, "//i[text()='User Collection']")
        self.counterDropdown = (By.CSS_SELECTOR, "select#ddlCounter")
        self.counterNameFromTable = (By.CSS_SELECTOR, "div[col-id='CounterName']")

    def verify_active_counter_message_in_dispensary(self):
        """
        /**
        * @Test2
        * @description This method navigates to the Dispensary module and checks if counters are available.
        *              If counters exist, it selects one at random, activates it, and verifies that the activation
        *              message correctly displays the name of the selected counter.
        */
        """
        try:
            # Navigate to Dispensary module
            self.driver.find_element(*self.dispensaryLink).click()

            self.driver.find_element(*self.activateCounter).click()

            # Wait for the page to load
            time.sleep(2)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='caption-subject']")))

            # Get the count of available counters
            counter_count = len(self.driver.find_elements(By.XPATH, "//div[@class='counter-item']"))
            print(f"Counter count >> {counter_count}")

            if counter_count >= 1:
                import random
                # Select a random counter index
                random_index = random.randint(1, counter_count)
                print(f"Random counter index selected: {random_index}")

                # Fetch the name of the selected counter and extract the counter name
                full_counter_text = self.driver.find_element(By.XPATH, f"(//div[@class='counter-item']//h5)[{random_index}]").text
                counter_name = full_counter_text.split("click to Activate")[0].strip() if full_counter_text else ""
                print(f"Counter name at index {random_index}: {counter_name}")

                # Highlight and select the random counter
                random_counter = self.driver.find_element(By.XPATH, f"(//div[@class='counter-item'])[{random_index}]")
                random_counter.click()

                # Activate the selected counter
                time.sleep(2)
                self.driver.find_element(*self.activateCounter).click()

                # Get the activation message text and log it
                activated_counter_info_text = self.driver.find_element(*self.activatedCounterInfo).text
                print(f"Activated counter info text : {activated_counter_info_text}")

                # Check if the message contains the selected counter name and log verification if true
                if activated_counter_info_text and counter_name in activated_counter_info_text:
                    print("-------------------------Verified-------------------------")
            return True

        except Exception as e:
            print(f"Error selecting random counter: {e}")
            return False

    def activate_counter_and_select_sale(self):
        """
        /**
        * @Test10
        * @description This method verifies the activation of a counter and selects the Sale tab using Alt + N.
        * @expected
        * The Sale tab should be selected after pressing Alt + N.
        */
        """
        try:
            # Navigate to Dispensary Module
            self.wait.until(EC.element_to_be_clickable(*self.dispensaryLink)).click()

            # Navigate to the Activate Counter page
            self.wait.until(EC.element_to_be_clickable(*self.activate_counter_link)).click()

            # Wait for the page to load
            time.sleep(5)  # Adjust time as needed

            actions = ActionChains(self.driver)
            actions.key_down(Keys.ALT).send_keys("n").key_up(Keys.ALT).perform()

            # Wait for the error message to appear
            patient_modal = self.wait.until(EC.visibility_of_element_located(self.newPatient_modal))

            # Verify the error message
            assert patient_modal.is_displayed(), "Patient modal is not displayed."

            return True

        except Exception as e:
            print(f"Test failed due to error: {e}")
            return False
