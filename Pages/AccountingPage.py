import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class AccountingPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.accounting = {
            "accounting_link": (By.CSS_SELECTOR, 'a[href="#/Accounting"]'),
            "reports_link": (By.XPATH, "//a[contains(text(),'Reports')]"),
            "daily_transactions_report": (By.XPATH, "//i[text()='Daily Transaction']"),
            "fiscal_year_dropdown": (By.XPATH, "//label[@class='control-label']/../div//select"),
            "fiscal_year_2023": (By.XPATH, "//option[contains(text(),'2023')]"),
            "load_button": (By.XPATH, "//button[contains(text(),'Load')]"),
            "results_table": (By.CSS_SELECTOR, "div[ref='gridPanel']"),
        }

    def load_daily_transactions_report(self):
        """
        /**
        * @Test12
        * @description This method verifies the loading of the Daily Transactions Report.
        * It navigates to the Accounting Reports page, selects the report,
        * chooses the fiscal year, and clicks the Load button.
        * @expected
        * The Daily Transactions Report should be loaded successfully.
        */
        """
        try:
            # Click on the Accounting Module
            self.wait.until(EC.element_to_be_clickable(self.accounting["accounting_link"])).click()

            # Select Daily Transactions Report
            self.wait.until(EC.element_to_be_clickable(self.accounting["reports_link"])).click()
            self.wait.until(EC.element_to_be_clickable(self.accounting["daily_transactions_report"])).click()

            # # Choose 2023 as the Fiscal Year
            # self.wait.until(EC.element_to_be_clickable(self.accounting["fiscal_year_dropdown"])).click()
            # self.wait.until(EC.element_to_be_clickable(self.accounting["fiscal_year_2023"])).click()

            # Locate the dropdown
            dropdown = self.driver.find_element(By.XPATH, "//label[@class='control-label']/../div//select")

            # Create Select object
            select = Select(dropdown)

            # Select by visible text
            select.select_by_visible_text("2023")

            # Click on the Load button
            self.wait.until(EC.element_to_be_clickable(self.accounting["load_button"])).click()

            # Wait for the page to load
            time.sleep(3)

            results_table = self.wait.until(EC.visibility_of_element_located(self.accounting["results_table"]))

            # Verify the error message
            assert results_table.is_displayed(), "Table is not displayed."

            return True

        except Exception as e:
            print(f"Test failed due to error: {e}")
            return False