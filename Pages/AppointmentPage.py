from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.appointment = {
            "appointment_link": (By.CSS_SELECTOR, 'a[href="#/Appointment"]'),
            "counter_item": (By.XPATH, "//div[@class='counter-item']"),
            "patient_name": (By.XPATH, "//div[@role='gridcell' and @col-id='ShortName'][1]"),
            "search_bar": (By.CSS_SELECTOR, "#quickFilterInput"),
            "appointment_booking_list": (By.CSS_SELECTOR, "ul.page-breadcrumb li a[href='#/Appointment/ListAppointment']"),
            "visit_type_dropdown": (By.NAME, "VistType"),
            "from_date": (By.XPATH, "(//input[@id='date'])[1]"),
            "show_patient": (By.XPATH, "//button[contains(text(),'Show Patient')]"),
            "visit_type_column": (By.XPATH, "//div[@col-id='AppointmentType']"),
        }

    def verify_patient_name(self) -> bool:
        """
        /**
        * @Test1
        *
        * @description This method verifies whether a patient search returns the correct result.
        * @return boolean - Returns True if the search result matches the patient name, otherwise False.
        */
        """
        try:
            self.driver.find_element(*self.appointment["appointment_link"]).click()
            time.sleep(10)

            counter_items = self.driver.find_elements(*self.appointment["counter_item"])
            if len(counter_items) > 0:
                counter_items[0].click()

            patient_name = self.driver.find_element(*self.appointment["patient_name"]).text
            search_bar = self.driver.find_element(*self.appointment["search_bar"])
            search_bar.send_keys(patient_name)
            search_bar.send_keys(Keys.ENTER)
            time.sleep(4)

            result_text = self.driver.find_element(By.XPATH, "//div[@role='gridcell' and @col-id='ShortName']").text
            time.sleep(3)

            return result_text.strip() == patient_name.strip()
        except Exception as e:
            print(f"Error verifying patient name: {e}")
            return False
