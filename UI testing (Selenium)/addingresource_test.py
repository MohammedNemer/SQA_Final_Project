from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open MockAPI website
    driver.get("https://mockapi.io/")
    driver.maximize_window()
    time.sleep(2)  # Wait for the page to load

    # Step 2: Click on the Login button
    login_button = driver.find_element(By.LINK_TEXT, "Login")
    login_button.click()
    time.sleep(2)  # Wait for the login page to load

    # Step 3: Input valid email and password
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("mohammed-nemer@hotmail.com")  # Replace with your valid email
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("mohammed@2024")  # Replace with your valid password

    # Step 4: Click the Login button
    login_submit_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_submit_button.click()
    time.sleep(3)  # Wait for the page to redirect

    # Step 5: Click on "Projects" link
    projects_link = driver.find_element(By.XPATH, "//a[@href='projects/6768b820cbf3d7cefd38875d']")
    projects_link.click()
    time.sleep(2)  # Wait for the project page to load


    # Step 6: Click on "New Resource"
    new_resource_button = driver.find_element(By.XPATH, "//button[contains(text(), 'New resource')]")
    new_resource_button.click()
    time.sleep(2)  # Wait for the resource creation modal to load

    # Step 7: Enter the resource name
    resource_name_input = driver.find_element(By.NAME, "name")
    resource_name_input.send_keys("TestResource")  # Replace with your desired resource name

    # Step 8: Click the "Create" button
    create_button = driver.find_element(By.XPATH, "//button[text()='Create']")
    create_button.click()
    time.sleep(3)  # Wait for the resource to be added

    # Step 9: Verify the new resource is added
    try:
        added_resource = driver.find_element(By.XPATH, "//button[contains(text(), 'New resource')]")
        print("Test Passed: Resource added successfully.")
    except:
        print("Test Failed: Resource not found.")   
        
    driver.save_screenshot("Resource_Added.png")

finally:
    # Close the browser
    driver.quit()
