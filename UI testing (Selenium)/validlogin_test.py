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

    # Step 3: Input valid email
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("mohammed-nemer@hotmail.com")  # Replace with your valid email

    # Step 4: Input valid password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("mohammed@2024")  # Replace with your valid password

    # Step 5: Click the Login button
    login_submit_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_submit_button.click()
    time.sleep(3)  # Wait for the page to redirect

    # Step 6: Verify successful login by checking the "Projects" element
    try:
        projects_element = driver.find_element(By.XPATH, "//div[contains(text(), 'Projects')]")
        print("Test Passed: Login successful, 'Projects' element found.")
    except:
        print("Test Failed: 'Projects' element not found.")
        
    driver.save_screenshot("Login Success.png")

finally:
    # Close the browser
    driver.quit()
