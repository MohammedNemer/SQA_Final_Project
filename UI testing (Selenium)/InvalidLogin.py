from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
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

    # Step 3: Input invalid email
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("invalidemail@example.com")

    # Step 4: Input invalid password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("wrongpassword")

    # Step 5: Click the Login button
    login_submit_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_submit_button.click()
    time.sleep(2)  # Wait for error message to appear

    # Step 6: Verify the error message
    try:
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Incorrect email/password combination')]")
        assert "Incorrect email/password combination" in error_message.text
        print("Test Passed: Error message displayed for invalid credentials.")
    except NoSuchElementException:
        print("Test Failed: Error message not found.")
        
    driver.save_screenshot("login_error_message.png")

finally:
    # Close the browser
    driver.quit()
