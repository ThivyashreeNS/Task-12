"""Login_page.py"""

# Import necessary modules from Selenium and other libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Resources.Locators import TestLocators
from Resources.Data import WebData
from Resources.ExcelFunctions import ExcelFunctions

import sys
import os
# Add the parent directory of Task_12 to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


# Class have the login page functionality
class LoginPage(WebData, TestLocators):
    # Constructor to initialize the login page with the provided WebDriver instance.
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Set an explicit wait to wait for elements to become interactable (up to 10 seconds)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        self.driver.get(self.url)
        # Initialize ExcelFunctions for data handling
        self.xlobj = ExcelFunctions(WebData().excel_file, WebData().sheet_number)

    # Login method using credentials from Excel.
    def login(self, username_row, password_row):
        # Read username and password from Excel
        username = self.xlobj.read_data(username_row, 2)
        password = self.xlobj.read_data(password_row, 3)

        try:
            # Wait for the username & password field and input data, then click login.
            self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().username_name))).send_keys(username)
            self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().password_name))).send_keys(password)
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().login_button))).click()

            # Check for error message if the login was unsuccessful
            try:
                error_element = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().error_element)))
                # If the error element is visible, get the error text
                if error_element.is_displayed():
                    error_text = error_element.text
                    print("Login failed:", error_text)
                    return self.driver.current_url, error_text  # Return current URL and error text
            # Return any exceptions encountered
            except Exception as error:
                print (error)

            print("Login successful.")
            return self.driver.current_url, None

        # Return current URL after successful login
        except Exception as error:
            print("Error during login:", error)
            return self.driver.current_url, error


    # Method to close the browser after all tests are completed
    def close_driver(self):
        self.driver.quit()


    # Tests case for first login scenario
    def TC_Login_01(self):
        # Call the login method from LoginPage
        return self.login(2, 2)

    # Tests case for second login scenario
    def TC_Login_02(self):
        return self.login(3, 3)

    # Tests case for third login scenario
    def TC_Login_03(self):
        return self.login(4, 4)

    # Tests case for fourth login scenario
    def TC_Login_04(self):
        return self.login(5, 5)

    # Tests case for fifth login scenario
    def TC_Login_05(self):
        return self.login(6, 6)

