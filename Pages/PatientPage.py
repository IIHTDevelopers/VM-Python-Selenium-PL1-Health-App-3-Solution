import os

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PatientPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.patient = {
            "patient_link": (By.CSS_SELECTOR, 'a[href="#/Patient"]'),
            "search_bar": (By.CSS_SELECTOR, "#quickFilterInput"),
            "register_patient": (By.CSS_SELECTOR, 'ul.page-breadcrumb a[href="#/Patient/RegisterPatient"]'),
            "new_photo_button": (By.XPATH, '//button[contains(text(),"New Photo")]'),
            "upload_button": (By.CSS_SELECTOR, 'label[for="fileFromLocalDisk"]'),
            "done_button": (By.XPATH, '//button[text()="Done"]'),
            "uploaded_img": (By.CSS_SELECTOR, 'div.wrapper img'),
            "profile_picture_icon": (By.CSS_SELECTOR, 'a[title="Profile Picture"]'),
        }

    def search_and_verify_patients(self, patient_data):
        """
        /**
        * @Test6
        * @description This method navigates to the patient section, iterates over a predefined list of patients,
        *              and performs a search operation for each patient name. After each search, it verifies that the
        *              search result matches the expected patient name. Returns True if all patient searches are verified
        *              successfully; returns False if an error occurs.
        */
        """
        try:
            # Highlight and click the patient link
            self.driver.find_element(*self.patient["patient_link"]).click()
            time.sleep(2)

            search_bar = self.driver.find_element(*self.patient["search_bar"])
            time.sleep(2)

            for patient_name in patient_data:
                print(f"Verifying patient: {patient_name}")

                # Enter patient name in the search bar
                search_bar.send_keys(patient_name)
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.ENTER).perform()
                time.sleep(3)

                # Capture the search result text
                result_text = self.driver.find_element(By.XPATH, "//div[@role='gridcell' and @col-id='ShortName']").text
                time.sleep(3)

                # Compare the result text with the expected patient name
                if result_text.strip() != patient_name.strip():
                    print(
                        f"Search result mismatch for patient: {patient_name}. Expected '{patient_name.strip()}', got '{result_text.strip()}'.")
                    return False

                # Clear the search bar for the next patient
                search_bar.send_keys("")

            return True

        except Exception as e:
            print(f"Error in searching and verifying patients: {e}")
            return False