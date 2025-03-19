import json
import pathlib
import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from Pages.AccountingPage import AccountingPage
from Pages.DispensaryPage import DispensaryPage
from Pages.LaboratoryPage import LaboratoryPage
from Pages.LoginPage import LoginPage
from Pages.AppointmentPage import AppointmentPage
from Pages.MaternityPage import MaternityPage
from Pages.NursingPage import NursingPage
from Pages.OperationTheatrePage import OperationTheatrePage
from Pages.ProcurementPage import ProcurementPage
from Pages.PatientPage import PatientPage
from Pages.RadiologyPage import RadiologyPage
from Pages.SettingsPage import SettingsPage
from tests.TestUtils import TestUtils


# Fixture to set up the WebDriver for each test function
@pytest.fixture(scope="function")
def setup_driver():
    """
    Initializes the WebDriver for Chrome and navigates to the application URL.
    Ensures the driver is properly closed after each test execution.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://healthapp.yaksha.com/')
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()

# Reusable login function to be called before each test
def login_to_application(driver):
    """
    Logs in to the application before each test.

    Args:
        driver (webdriver): Selenium WebDriver instance.
        test_credentials (dict): Dictionary containing username and password.
    """
    login_page = LoginPage(driver)
    login_page.perform_login()
    time.sleep(5)

@pytest.mark.order(1)
def test_verify_patient_name(setup_driver):
    """
    Test Case: Verify the user can search patient under appointment module and the searched patient is filtered out.

    Expected Result:
    - The 'Visit Type' column should contain only patients in the "new visit" category.
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    appointment_page = AppointmentPage(driver)
    testResult = appointment_page.verify_patient_name()
    time.sleep(5)
    verificationResult = verify_patient_search_happened(driver)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False


@pytest.mark.order(2)
def test_verify_active_counter_message_in_dispensary(setup_driver):
    """
    Test Case: Verify active counter message under Dispensar moduel

    Expected Result:
    - An alert with the message "Patient not Selected! Please Select the patient first!" is displayed and handled.
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    dispensaryPage = DispensaryPage(driver)
    testResult = dispensaryPage.verify_active_counter_message_in_dispensary()
    time.sleep(5)
    verificationResult = verify_dispensary_counter_activation(driver)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False


@pytest.mark.order(3)
def test_verify_purchase_request_list_elements(setup_driver):
    """
        Test Case: Verify the components of purchase requiest list are visible correctly under procurement module

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Doctors/OutPatientDoctor/NewPatient
        2. Click on the In Patient Department Tab.
        3. In the search bar, enter the patient name "Devid8 Roy8" and perform the search.
        4. Locate the patient in the results and click on the Preview icon under the Actions column.

        Expected Result:
        - Verify the same patient overview page is displayed with the same patient name.
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    procurementPage = ProcurementPage(driver)
    testResult = procurementPage.verify_purchase_request_list_elements()
    verificationResult = verify_user_is_on_correct_url(driver,"ProcurementMain/PurchaseRequest/PurchaseRequestList")
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False

@pytest.mark.order(4)
def test_verify_error_message(setup_driver):
    """
        Test Case: Verify the user gets error one adding new lab test without filling details

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Doctors/OutPatientDoctor/NewPatient
        2. Click on the In Patient Department Tab.
        3. In the search bar, enter the patient name "Devid173 Roy8" and perform the search.
        4. On the Patient Overview page, click on the Notes section..
        5. Now click on "Add Notes" button.
        6. Select Template as "Progress Note" from dropdown.
        7, Enter subjective Notes as "Test Notes" and click on save button.

        Expected Result:
        - A success confirmation popup with the message: "Progress Note Template added." should appear.
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    laboratoryPage = LaboratoryPage(driver)
    testResult = laboratoryPage.verify_error_message()
    verificationResult = check_error_message_occurs(driver)
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False

@pytest.mark.order(5)
def test_perform_radiology_request_and_handle_alert(setup_driver):
    """
        Test Case: Add and Verify New Currency in Settings

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/ProcurementMain/PurchaseRequest/PurchaseRequestList
        2. Click on the Settings tab then click on currency.
        3. Click on add currency button.
        4. Enter a unique currecny code and fill description .
        5. Now click on "Add Currency" button.

        Expected Result:
        - The new currency should be added successfully and displayed in the table with the correct currency code and description.
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    radiologyPage = RadiologyPage(driver)
    with open("C:/Users/testu/Downloads/YakshaPythonPL2Final/Data/testData.json", "r") as file:
        test_data = json.load(file)
    data = {
        "FromDate": str(test_data["DateRange"][0]["FromDate"])
    }
    testResult = radiologyPage.perform_radiology_request_and_handle_alert(data)
    verificationResult = verify_user_is_on_correct_url(driver,"Radiology/ImagingRequisitionList")
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False

@pytest.mark.order(6)
def test_search_and_verify_patients(setup_driver):
    """
        Test Case: Verify the user can search and verify the patients exists on the patient module

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Utilities
        2. Click on the Scheme Refund Tab.
        3. Click on "New scheme Refund Entry" button.
        4. Now click on save without entering value in any field.

        Expected Result:
        - A warning popup with the message: "Please fill all the mandatory fields."
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    patientPage = PatientPage(driver)
    with open("C:/Users/testu/Downloads/YakshaPythonPL2Final/Data/testData.json", "r") as file:
        test_data = json.load(file)
    patient_data = [list(patient.values())[0] for patient in test_data["PatientNames"]]
    testResult = patientPage.search_and_verify_patients(patient_data)
    verificationResult = verify_user_is_on_correct_url(driver,"Patient/SearchPatient")
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False

@pytest.mark.order(7)
def test_verify_notice_message_after_entering_incorrect_filters(setup_driver):
    """
        Test Case: Verify notice message after entering incorrect filters

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/
        2. Click on the Admin dropdown.
        3. Select the "My Profile" option.

        Expected Result:
        - Verify that the user is redirected to the "User Profile" page and the page header or title confirms this.
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    procurementPage = ProcurementPage(driver)
    testResult = procurementPage.verify_notice_message_after_entering_incorrect_filters()
    verificationResult = verify_date_filter_error_message(driver)
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False

@pytest.mark.order(8)
def test_verify_maternity_allowance_report(setup_driver):
    """
        Test Case: Verify Maternity Allowance Payment Receipt Modal

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Maternity/PatientList
        2. Click on the Reports submodule.
        3. Select Maternity Allowance Report, enter the From Date as 01-01-2020, and click the OK button.
        4. From the table, click on View Details for the first record.
        5. Verify that the "Maternity Allowance Payment Receipt" modal appears.

        Expected Result:
        - Verify that the "Maternity Allowance Payment Receipt" modal appears.
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    maternityPage = MaternityPage(driver)
    testResult = maternityPage.verify_maternity_allowance_report()
    verificationResult = verify_user_is_on_correct_url(driver,"/Maternity/Reports/MaternityAllowance")
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False

@pytest.mark.order(9)
def test_verify_occupied_bed_edit(setup_driver):
    """
        Test Case: Verify Error Message When Editing an Occupied Bed

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Settings/ADTManage/ManageWard
        2. Click on the Manage Bed tab.
        3. Locate any occupied bed and click the Edit button.
        4. Verify that an error message "Cannot modify occupied beds." is displayed.

        Expected Result:
        - Clicking Edit on an occupied bed should not allow modifications and should display the error message "Cannot modify occupied beds."
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    settingsPage = SettingsPage(driver)
    testResult = settingsPage.verify_occupied_bed_edit()
    verificationResult = verify_user_is_on_correct_url(driver, "/Settings/ADTManage/ManageBed")
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False

@pytest.mark.order(10)
def test_activate_counter_and_select_sale(setup_driver):
    """
        Test Case: Verify Add New Patient modal opens with Alt + Enter keyboard shortcut

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Dispensary/ActivateCounter
        2. Activate any counter.
        3. Select the Sale tab and press Alt + N.

        Expected Result:
        - Add New Patient modal should open."
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    dispensaryPage = DispensaryPage(driver)
    testResult = dispensaryPage.activate_counter_and_select_sale()
    verificationResult = verify_user_is_on_correct_url(driver, "/Dispensary/Sale/New")
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False

@pytest.mark.order(11)
def test_verify_ot_booking(setup_driver):
    """
        Test Case: Verify Remarks text field placeholder value

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/OperationTheatre/OtBookingList
        2. Click on new OT booking button.
        3. Verify Remarks Text area is enable
        4. Verify the placeholder name of Remarks text area.

        Expected Result:
        - Verify the placeholder name of Remarks text area.
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    ot_Page = OperationTheatrePage(driver)
    testResult = ot_Page.verify_ot_booking()
    verificationResult = verify_user_is_on_correct_url(driver, "/OperationTheatre/OtBookingList")
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False

@pytest.mark.order(12)
def test_load_daily_transactions_report(setup_driver):
    """
        Test Case: Verify Daily Transactions Report for

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Accounting/Reports
        2. Select Daily Transactions Report from the available reports.
        3. Choose 2023 as the Fiscal Year.
        4. Click on the Load button.

        Expected Result:
        - Clicking on Load should populate the table with relevant transaction data
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    accountingPage = AccountingPage(driver)
    testResult = accountingPage.load_daily_transactions_report()
    verificationResult = verify_user_is_on_correct_url(driver, "/Accounting/Reports/DailyTransactionReport")
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False

@pytest.mark.order(13)
def test_search_patient_and_view_overview(setup_driver):
    """
        Test Case: Verify Navigation to Patient Overview from Past Days Records

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Nursing/OutPatient
        2. Click on the Past Days tab.
        3. Enter the From Date as 01-01-2020 and click the OK button.
        4. Search for the patient "Deepika Rani" in the list.
        5. Locate the patient’s record and click on Overview from the Actions column.

        Expected Result:
        - Clicking on Overview should navigate the user to the Patient Overview page successfully.
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    nursingPage = NursingPage(driver)
    testResult = nursingPage.search_patient_and_view_overview()
    verificationResult = verify_user_is_on_correct_url(driver, "/Nursing/PatientOverviewMain/PatientOverview")
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False

@pytest.mark.order(14)
def test_filter_sample_collections(setup_driver):
    """
        Test Case: Verify table filtering for "Male Ward"

        Steps:
        1. Navigate to https://healthapp.yaksha.com/Home/Index#/Lab/Dashboard
        2. Select the Sample Collections tab.
        3. Enter From Date as 01-01-2020 and click OK.
        4. Hover over the Item column and click Hamburger Menu.
        5. Select Equals from the dropdown.
        6. Enter Male Ward in the text field.

        Expected Result:
        - Table should display only rows with "Male Ward" in the Item column.
    """
    test_obj = TestUtils()
    driver = setup_driver
    login_to_application(driver)  # Perform login before test
    labPage = LaboratoryPage(driver)
    testResult = labPage.filter_sample_collections()
    verificationResult = verify_user_is_on_correct_url(driver, "/Nursing/PatientOverviewMain/PatientOverview")
    time.sleep(5)
    if (testResult == True and verificationResult == True):
        passed = True
        test_obj.yakshaAssert("TestValidLogin", True, "healthapp")
        print("TestValidLogin = Passed")
        assert True
    else:
        passed = False
        test_obj.yakshaAssert("TestValidLogin", False, "healthapp")
        print("TestValidLogin = Failed")
        assert False


"""------------------------------------------------- Helper Method------------------------------------------------------------"""


def verify_patient_search_happened(driver) -> bool:
    """
    /**
    * @description This method verifies if a patient search has occurred by checking
    *              if the patient list contains exactly one result.
    * @return boolean - Returns True if the search happened, otherwise False.
    */
    """
    try:
        patient_list = driver.find_elements(By.XPATH, "//div[@role='gridcell' and @col-id='ShortName']")
        if len(patient_list) == 1:
            print("Patient search happened")
            return True
        else:
            raise Exception("Patient search didn't happen")
    except Exception as e:
        print(f"Error verifying patient search: {e}")
        return False

def verify_dispensary_counter_activation(driver) -> bool:
    """
    /**
    * @description This method verifies if the dispensary counter is activated by checking
    *              the visibility of the 'Deactivate Counter' button.
    * @return boolean - Returns True if the button is visible, otherwise False.
    */
    """
    try:
        is_visible = driver.find_element(By.XPATH, "//button[contains(text(),'Deactivate Counter')]")
        return is_visible
    except Exception as e:
        print(f"Error verifying dispensary counter activation: {e}")
        return False

def verify_user_is_on_correct_url(driver, expected_url):
    """
    /**
    * @Test
    * @description This method verifies that the user is on the expected URL.
    * @expected
    * The current URL should contain the expected URL.
    */
    """
    try:
        WebDriverWait(driver, 10).until(lambda d: expected_url in d.current_url)
        return expected_url in driver.current_url
    except Exception as e:
        print(f"URL verification failed: {e}")
        return False

def check_error_message_occurs(driver) -> bool:
    """
    /**
    * @description This method verifies if an error message occurs by closing the modal
    *              and checking if the URL contains 'Lab/Settings/LabTest'.
    * @param page - Playwright page instance.
    * @return boolean - Returns True if the expected URL is found, otherwise False.
    */
    """
    try:
        close_button = driver.find_element(By.XPATH('//button[contains(text(),"Close")]'))
        close_button.click()

        return "Lab/Settings/LabTest" in driver.URL
    except Exception as e:
        print(f"Error while checking error message: {e}")
        return False

def verify_date_filter_error_message(driver) -> bool:
    """
    /**
    * @description This method verifies the error message displayed after entering an invalid date in the filter.
    * @param page - Playwright page instance.
    * @return boolean - Returns True if the error message is verified successfully, otherwise False.
    */
    """
    try:
        invalid_msg = driver.find_element(By.XPATH("//div[contains(@class,'invalid-msg-cal')]"))
        error_message = invalid_msg.text
        if invalid_msg.is_visible() and error_message.strip() == "Date is not between Range. Please enter again":
            return True
        return False
    except Exception as e:
        print(f"Error verifying date filter error message: {e}")
        return False

def verify_user_is_logged_in(driver) -> bool:
    """
    /**
    * @description This method verifies if the user is successfully logged in by checking
    *              if the 'admin' dropdown element is visible on the page.
    * @return boolean - Returns True if the user is logged in, otherwise False.
    */
    """
    try:
        # Wait for the dropdown element to be visible
        driver.find_element(By.XPATH, "//li[@class='dropdown dropdown-user'']")

        # Verify visibility of the dropdown element
        return driver.find_element(By.XPATH, "//li[@class='dropdown dropdown-user']").is_displayed()


    except Exception as e:
        print(f"Error verifying user login: {e}")
        return False

def verify_patient_search_happened(driver) -> bool:
    """
    /**
    * @description This method verifies if a patient search has occurred by checking
    *              if the patient list contains exactly one result.
    * @return boolean - Returns True if the search happened, otherwise False.
    */
    """
    try:
        patient_list = driver.find_elements(By.XPATH, "//div[@role='gridcell' and @col-id='ShortName']")
        if len(patient_list) == 1:
            print("Patient search happened")
            return True
        else:
            raise Exception("Patient search didn't happen")
    except Exception as e:
        print(f"Error verifying patient search: {e}")
        return False

def verify_dispensary_counter_activation(driver) -> bool:
    """
    /**
    * @description This method verifies if the dispensary counter is activated by checking
    *              the visibility of the 'Deactivate Counter' button.
    * @return boolean - Returns True if the button is visible, otherwise False.
    */
    """
    try:
        is_visible = driver.find_element(By.XPATH, "//button[contains(text(),'Deactivate Counter')]")
        return is_visible
    except Exception as e:
        print(f"Error verifying dispensary counter activation: {e}")
        return False

def verify_report_generation(driver) -> bool:
    """
    /**
    * @description This method verifies whether a report is generated by checking
    *              if there is more than one entry in the report table.
    * @return boolean - Returns True if the report contains more than one entry, otherwise False.
    */
    """
    try:
        table_length = len(driver.find_elements(By.CSS_SELECTOR, 'div[col-id="CounterName"]'))
        return table_length > 1
    except Exception as e:
        print(f"Error verifying report generation: {e}")
        return False

def verify_user_is_on_correct_url(driver, expected_url: str) -> bool:
    """
    /**
    * @description This method verifies if the user is on the correct URL by comparing
    *              the current page URL with the expected URL.
    * @param page - Playwright page instance.
    * @param expected_url - The expected URL substring to validate.
    * @return boolean - Returns True if the actual URL contains the expected URL, otherwise False.
    */
    """
    try:
        actual_url = driver.URL
        return expected_url in actual_url
    except Exception as e:
        print(f"Error verifying URL: {e}")
        return False

def verify_utilities_url(driver, expected_url: str) -> bool:
    """
    /**
    * @description This method navigates to the Utilities module, clicks on the "Change Billing Counter" option,
    *              and verifies if the user is redirected to the expected URL.
    * @param page - Playwright page instance.
    * @param expected_url - The expected URL substring to validate.
    * @return boolean - Returns True if the actual URL contains the expected URL, otherwise False.
    */
    """
    try:
        utilities_module = driver.find_element(By.XPATH("//span[text()='Utilities']"))
        change_billing_counter = driver.find_element(By.XPATH('//a[text()= " Change Billing Counter "]'))

        # Navigate to Utilities Module
        utilities_module.click()

        # Click on Change Billing Counter and measure load time
        change_billing_counter.click()

        actual_url = driver.URL
        return expected_url in actual_url
    except Exception as e:
        print(f"Error verifying Utilities URL: {e}")
        return False

def verify_purchase_req_data_is_present(driver) -> bool:
    """
    /**
    * @description This method verifies whether purchase request data is present in the table by
    *              checking if at least one entry exists in the "RequestDate" column.
    * @param page - Playwright page instance.
    * @return boolean - Returns True if at least one record is found, otherwise False.
    */
    """
    try:
        table_data = driver.find_element(By.XPATH('div[ref="eCenterContainer"] div[col-id="RequestDate"]'))
        return len(table_data) >= 1
    except Exception as e:
        print(f"Error verifying purchase request data presence: {e}")
        return False

def verify_user_is_not_logged_in(driver) -> bool:
    """
    /**
    * @description This method verifies that the user login attempt failed by checking
    *              if the 'Invalid credentials' error message is displayed.
    * @param page - Playwright page instance.
    * @return boolean - Returns True if the error message is visible, otherwise False.
    */
    """
    try:
        error_message = driver.find_element(By.XPATH('//div[contains(text(),"Invalid credentials !")]'))
        return error_message.is_visible()
    except Exception as e:
        print(f"Error verifying user login failure: {e}")
        return False

def check_error_message_occurs(driver) -> bool:
    """
    /**
    * @description This method verifies if an error message occurs by closing the modal
    *              and checking if the URL contains 'Lab/Settings/LabTest'.
    * @param page - Playwright page instance.
    * @return boolean - Returns True if the expected URL is found, otherwise False.
    */
    """
    try:
        close_button = driver.find_element(By.XPATH('//button[contains(text(),"Close")]'))
        close_button.click()

        return "Lab/Settings/LabTest" in driver.URL
    except Exception as e:
        print(f"Error while checking error message: {e}")
        return False

def is_hover_used(method) -> bool:
    """
    /**
    * @description This method checks if the given function contains the '.hover' keyword.
    * @param method - Function to inspect.
    * @return boolean - Returns True if '.hover' is found in the function, otherwise False.
    */
    """
    try:
        method_string = inspect.getsource(method)  # Get method source code as a string
        return ".hover" in method_string
    except Exception as e:
        print(f"Error inspecting method: {e}")
        return False

def verify_date_filter_error_message(driver) -> bool:
    """
    /**
    * @description This method verifies the error message displayed after entering an invalid date in the filter.
    * @param page - Playwright page instance.
    * @return boolean - Returns True if the error message is verified successfully, otherwise False.
    */
    """
    try:
        invalid_msg = driver.find_element(By.XPATH("//div[contains(@class,'invalid-msg-cal')]"))
        error_message = invalid_msg.text
        if invalid_msg.is_visible() and error_message.strip() == "Date is not between Range. Please enter again":
            return True
        return False
    except Exception as e:
        print(f"Error verifying date filter error message: {e}")
        return False

def verify_visit_page_opens(driver) -> bool:
    """
    /**
    * @description This method verifies if the visit page opens successfully by checking the visibility of the heading.
    * @param page - Playwright page instance.
    * @return boolean - Returns True if the visit page is visible, otherwise False.
    */
    """
    try:
        # self.driver = setup_driver;
        visit_page = driver.find_element(By.XPATH('//h3[contains(@class,"heading")]'))
        return visit_page.is_visible()
    except Exception as e:
        print(f"Error verifying visit page: {e}")
        return False

def verify_imaging_type_added(driver) -> bool:
    """
    /**
    * @description This method verifies whether the Imaging Type page is opened successfully.
    * @param page - Playwright page instance.
    * @return boolean - Returns True if the URL contains 'Settings/RadiologyManage/ManageImagingType', otherwise False.
    */
    """
    try:
        return "Settings/RadiologyManage/ManageImagingType" in driver.URL
    except Exception as e:
        print(f"Error verifying imaging type addition: {e}")
        return False