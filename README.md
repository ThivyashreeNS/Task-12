# Login Automation Project

## Overview:
This project automates the login process of an application using Selenium WebDriver, following a Data-Driven Testing (DDT) approach and Page Object Model (POM) design pattern. 
The test cases read login data (usernames, passwords, expected results) from an Excel file and perform login actions based on the provided credentials.

## Table of Contents:
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Code Explanation](#Code-Explanation)
- [Running the Tests](#running-the-tests)

## Features
- **Page Object Model (POM)**: The LoginPage class abstracts all interactions with the login page, making it easier to maintain and update tests if the UI changes.
  
- **Excel Integration**: Reads from and writes test data to an Excel file for easy management and reporting.
  
- **Reusable Components**: Common functions and data are abstracted into separate modules for better maintainability.
  
- **Dynamic Waits**: Uses explicit waits for web elements to ensure stability during testing.
  
- **Data-Driven Testing Framework**: Test data such as usernames, passwords, and expected results are fetched from an Excel file (test_data.xlsx).
 Each test case is executed with different data, allowing for scalable and maintainable tests.
  
- **Automation Framework**: Built using Selenium for browser automation and Pytest for test case management.

## Prerequisites
- Python 3.x
- Required libraries:
  - `selenium`
  - `pytest`
  - `openpyxl`
  - `webdriver-manager`

## Installation
To successfully set up and run the Selenium Automation Testing Project, follow these steps:

1. Ensure that you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/).

2. Familiarity with command-line interface (CLI) tools is recommended for executing commands.

3. Set Up a Virtual Environment (Optional but Recommended):
   - It's best practice to create a virtual environment to manage dependencies for your project:
     
     - Verify Python Virtual Environment: `Virtualenv --version`
       
     - Create Virtual Environment:  `virtualenv cd`
       
     - Activate Virtual Environment:  `Scripts\Activate`
       
     - Deactivate Virtual Environment: `Scripts\Deactivate`
       
4.  Install Required Libraries:
    - Install the necessary Python libraries using pip. The required libraries for this project include:
      - __Selenium :__ For web browser automation.
        Install Python Selenium Module: `pip install selenium`
        
      - __Pytest :__ For running test cases and managing test execution.
        `pip install pytest`
         Pytest Report: `pip install pytest-html`
        
      - __openpyxl :__ For reading and writing Excel files.
         `pip install selenium openpyxl`
        
      - __Webdriver-manager :__ To automatically manage browser drivers.
          Install WebDriver Manager Module: `pip install webdriver-manager`

## Project Structure:
```python
Task_12/
├── Resources/
│   ├── Data.py                               # Contains the WebData class for test data and configuration.
│   │   └── class WebData:
│   ├── Locators.py                           # Defines the TestLocators class for web element locators.
│   │   └── class TestLocators:
│   ├── ExcelFunctions.py                     # Contains the ExcelFunctions class for reading and writing Excel files.
│   │   └── class ExcelFunctions:
├── Pages/
│   ├── Login_page.py                         # Contains the LoginPage class for login functionality (POM).
│   │   ├── def login(username, password):    # Login method that uses data-driven test data.
│   │   ├── def TC_Login_01():                # Test case for Login scenario 1 (using DDT).
│   │   ├── def TC_Login_02():                # Test case for Login scenario 2 (using DDT).
│   │   ├── def TC_Login_03():                # Test case for Login scenario 3 (using DDT).
│   │   ├── def TC_Login_04():                # Test case for Login scenario 4 (using DDT).
│   │   ├── def TC_Login_05():                # Test case for Login scenario 5 (using DDT).
│   │   └── def close_driver():               # Close the WebDriver instance after each test case.
├── Tests/
│   ├── test_login_page.py                    # Test cases for login functionality (Data-Driven, using POM).
│   │   ├── def test_TC_Login_01():           # Test case for login scenario 1 (using data from Excel).
│   │   ├── def test_TC_Login_02():           # Test case for login scenario 2 (using data from Excel).
│   │   ├── def test_TC_Login_03():           # Test case for login scenario 3 (using data from Excel).
│   │   ├── def test_TC_Login_04():           # Test case for login scenario 4 (using data from Excel).
│   │   └── def test_TC_Login_05():           # Test case for login scenario 5 (using data from Excel).
│   │
├── Resources/
│   ├── test_data.xlsx                        # Excel file containing test data (usernames, passwords, expected results).
│
└── reports/
    └── loginTestReport.html                  # Pytest HTML Report for login tests.
```

## Code Explanation
- __Resources:__
Contains configuration data, such as search parameters, and locators for the page elements.

  -  __Data.py:__ Contains the WebData class, which holds test data (URLs and Excel file path) and configuration for the automation.
 
  -  __Locators.py:__  Defines the TestLocators class, which stores the locators for web elements such as the username, password fields, and the login button.
 
  - __ExcelFunctions.py:__
    - Contains the ExcelFunctions class that provides methods for reading and writing data to/from an Excel sheet.
    -  It is responsible for fetching the test data (usernames, passwords, etc.) and updating the Excel file with the test results.
    
- __Pages:__
  - __Login_page.py:__ 
    -  Contains the LoginPage class that represents the login page of the web application.
      
    -  It includes methods for logging in, checking login success, and handling errors.
  
- __Tests:__
  - __test_login_page.py:__ 
    -  Contains test cases that use pytest to validate the login functionality.
      
    -  Each test case corresponds to a row in the Excel file, which provides different credentials for the login.

- __Reports:__
  - __login.html:__ 
    -  HTML report generated by pytest after running the tests.
      
    -  It shows the results of each test case, including success or failure status and detailed logs.
   
- __Excel File:__
  - __test_data.xlsx:__ 
    - This Excel file holds the test data for the login scenarios. 
      
    - Each row contains a set of test data for a particular login test case (e.g., username, password).
   
## Running the test:
- To run the tests using pytest, run the following command:

  ```
      pytest -v -s --capture=sys --html=Reports\login.html Tests\test_login_page.py
  ```
  





