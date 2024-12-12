"""test_login_page.py"""

import pytest
from Resources.Data import WebData
from Pages.Login_page import LoginPage
from Resources.ExcelFunctions import ExcelFunctions


# Initialize common resources
excel_file = WebData().excel_file
sheet_number = WebData().sheet_number
# Creates an instance of ExcelFunctions which handles Excel operations.
xlobj = ExcelFunctions(excel_file, sheet_number)


# Define a test function for the first login test case.
def test_TC_Login_01():
    # Get an instance of the LoginPage class.
    shree = LoginPage()
    # Call the login test case method and get the current URL after login
    current_url, error = shree.TC_Login_01()
    # Check if the current URL matches the expected dashboard URL.
    if current_url == WebData.dashboard_url:
        # If logged in successfully, write a success message to the Excel file.
        xlobj.write_data(2, 8, "Tests Passed.")
        assert True
    else:
        # If login failed, write an error message to the Excel file.
        xlobj.write_data(2, 8, "Tests Failed")
        assert False

    # Close the driver after the test
    shree.close_driver()


# Define a test function for the second login test case.
def test_TC_Login_02():
    # Get an instance of the LoginPage class.
    shree = LoginPage()
    # Call the login test case method and get the current URL after login
    current_url, error = shree.TC_Login_02()
    # Check if the current URL matches the expected dashboard URL.
    if current_url == WebData.dashboard_url:
        # If logged in successfully, write a success message to the Excel file.
        xlobj.write_data(3, 8, "Tests Passed.")
        assert True
    else:
        # If login failed, write an error message to the Excel file.
        xlobj.write_data(3, 8, "Tests Failed")
        assert False
    # Close the driver after the test
    shree.close_driver()


# Define a test function for the third login test case.
def test_TC_Login_03():
    shree = LoginPage()
    current_url, error = shree.TC_Login_03()
    if current_url == WebData.dashboard_url:
        xlobj.write_data(4, 8, "Tests Passed.")
        assert True
    else:
        xlobj.write_data(4, 8, "Tests Failed")
        assert False
    shree.close_driver()

# Define a test function for the fourth login test case.
def test_TC_Login_04():
    shree = LoginPage()
    current_url, error = shree.TC_Login_04()
    if current_url == WebData.dashboard_url:
        xlobj.write_data(5, 8, "Tests Passed.")
        assert True
    else:
        xlobj.write_data(5, 8, "Tests Failed")
        assert False
    shree.close_driver()

# Define a test function for the fifth login test case.
def test_TC_Login_05():
    shree = LoginPage()
    current_url, error = shree.TC_Login_05()
    if current_url == WebData.dashboard_url:
        xlobj.write_data(6, 8, "Tests Passed.")
        assert True
    else:
        xlobj.write_data(6, 8, "Tests Failed")
        assert False
    shree.close_driver()












