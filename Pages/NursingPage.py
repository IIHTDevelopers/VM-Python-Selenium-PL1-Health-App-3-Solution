import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NursingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.outpatient = {
            "nursing_link": (By.CSS_SELECTOR, 'a[href="#/Nursing"]'),
            "past_days_tab": (By.XPATH, "//a[text()='Past Days']"),
            "from_date_input": (By.XPATH, "(//input[@id='date'])[1]"),
            "ok_button": (By.XPATH, "//button[contains(text(),'OK')]"),
            "search_input": (By.XPATH, "//input[@id='quickFilterInput']"),
            "patient_record": (By.CSS_SELECTOR, "i[title='overview']"),
            "patient_overview": (By.CSS_SELECTOR, "h1.pat-name-hd"),
        }

    def search_patient_and_view_overview(self):
        """
        /**
        * @Test13
        * @description This method verifies the functionality of searching for a patient
        * and viewing their overview in the OutPatient section.
        * It navigates to the OutPatient page, clicks on the Past Days tab,
        * enters the From Date, searches for the patient, and clicks on Overview.
        * @expected
        * The Overview for the patient "Deepika Rani" should be displayed.
        */
        """
        try:
            # Click on the Nursing Module
            self.wait.until(EC.element_to_be_clickable(self.outpatient["nursing_link"])).click()

            # Click on the Past Days tab
            self.wait.until(EC.element_to_be_clickable(self.outpatient["past_days_tab"])).click()

            # Enter the From Date
            from_date_input = self.wait.until(EC.visibility_of_element_located(self.outpatient["from_date_input"]))
            from_date_input.clear()  # Clear any existing text
            from_date_input.send_keys("01-01-2020")

            # Click the OK button
            self.wait.until(EC.element_to_be_clickable(self.outpatient["ok_button"])).click()

            # Wait for the results to load
            time.sleep(2)  # Adjust this time as necessary for the results to load

            # Search for the patient "Deepika Rani"
            search_input = self.wait.until(EC.visibility_of_element_located(self.outpatient["search_input"]))
            search_input.clear()  # Clear any existing text
            search_input.send_keys("Deepika Rani")

            # Wait for the search results to update
            time.sleep(2)  # Adjust this time as necessary for the search results to load

            # Locate the patient's record and click on Overview from the Actions column
            self.wait.until(EC.element_to_be_clickable(self.outpatient["patient_record"])).click()

            patient_overview = self.wait.until(EC.visibility_of_element_located(self.outpatient["patient_overview"]))

            # Verify the error message
            assert patient_overview.is_displayed(), "Patient Overview Page is not displayed."

            print("Overview for patient 'Deepika Rani' is displayed successfully.")

            return True

        except Exception as e:
            print(f"Test failed due to error: {e}")
            return False