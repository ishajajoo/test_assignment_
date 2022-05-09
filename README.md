
Python Test Automation Framework

**Description:**

Test Automation Framework using Python and pytest with the below features:

1. Framework is based on page object model where logics, tests and config are kept independently
2. Reporting using Allure report.
3. Copy binary file from source path and create a file with the same name in the destination path

**Install dependencies:**

Install the dependent packages in requirements.txt using pip install -r requirements.txt

To execute the program, follow the below steps:

1. Execute command "pytest --alluredir=allure_report tests/test_dothings.py <input_path> <output_path> in Terminal
2. allure serve allure_reports

**Results:** 
1. The file from source path will be copied and saved to the destination path
2. Assertions will be Validated against the test cases
3. Allure report with Pass/Fail status is generated
4. Log is generated