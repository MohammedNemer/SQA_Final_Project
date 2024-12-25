# SQA_Final_Project
## **Project Overview**
This repository contains all the files and resources for the **Software Quality Assurance Fundamentals Final Project**. The project involves performing API testing using Postman and UI testing using Selenium for the MockAPI application.

### **Objectives:**
1. Validate API functionality and error handling.
2. Simulate user interactions with the MockAPI interface.
3. Test the application's performance and reliability under load.
4. Document all findings in a comprehensive project report.

---

## **Contents**
1. **API Testing**:
   - Postman collections and test results for CRUD operations.
   - Performance and reliability test files (e.g., load and stress testing).
2. **UI Testing**:
   - Selenium scripts for login, resource management, and page navigation.
   - Screenshots for key scenarios (valid/invalid login, resource actions).
3. **Project Report**:
   - Detailed report summarizing the testing process, test cases, results, and recommendations.

---

## **How to Run the Tests**

### **1. API Testing (Postman):**
1. Import the `.json` files in the `API_Testing` folder into Postman.
2. Run the collection using Postman’s **Collection Runner**:
   - Configure iterations, delays, or performance settings as required.
3. Observe the results in the runner or export them as `.json` reports.

### **2. UI Testing (Selenium):**
1. Install required Python packages:
   ```bash
   pip install selenium webdriver-manager
   ```
2. Run the Python scripts for each test case:
   ```bash
   python validlogin_test.py
   python addingresource_test.py
   python resourceDeleting_test.py
   python InvalidLogin.py
   python EditingResource_test.py
   ```
3. Ensure **ChromeDriver** is installed and accessible in your system.

---

## **Test Cases**
The following test cases were executed for both API and UI testing:

### **API Test Cases**
1. **GET All Tasks**: Retrieve all tasks from the endpoint.
2. **GET Non-Existent Task**: Handle non-existent task retrieval.
3. **POST Valid Task**: Create a new task with valid data.
4. **POST Invalid URL**: Handle invalid endpoint errors.
5. **PUT Update Task**: Update an existing task.
6. **PUT Non-Existent Task**: Handle update for non-existent tasks.
7. **DELETE Existing Task**: Delete a task successfully.
8. **DELETE Non-Existent Task**: Handle deletion of non-existent tasks.

### **UI Test Cases**
1. **Valid Login**: Verify successful login with correct credentials.
2. **Invalid Login**: Validate error handling for invalid credentials.
3. **Add Resource**: Test resource creation functionality.
4. **Edit Resource**: Test resource update functionality.
5. **Delete Resource**: Validate resource deletion and modal interaction.

---

## **Project Report**
The full project report is included as a PDF file in the repository. It provides:
- Application and API analysis.
- Detailed test cases for API and UI.
- Results of both successful and failed scenarios.
- Observations from performance and reliability tests.

---

## **Tools and Technologies**
1. **Postman**: For API testing and automation.
2. **Selenium**: For UI testing and automation.
3. **Python**: Backend scripting for Selenium test cases.
4. **MockAPI**: Application under test.
5. **GitHub**: Version control and project repository.

---

## **How to Contribute**
1. Clone the repository:
   ```bash
   git clone https://github.com/MohammedNemer/SQA_Final_Project.git
   ```
2. Make changes or improvements.
3. Commit your changes:
   ```bash
   git commit -m "Your message here"
   ```
4. Push the changes:
   ```bash
   git push origin main
   ```

---

## **Contributors**
1. **Mohammed Sadi Mahmoud Nemer** (2020089)  
2. **Mohmad Moaena** (2019759)  
3. **Rayan Abu Gharbieh** (2100497)  
4. **Qamar Mourad** (2104729)

---

**Submission Date**: December 24, 2024
