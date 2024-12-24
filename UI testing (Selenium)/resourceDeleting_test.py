from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # Step 5: Click on the "Projects" link
    projects_link = driver.find_element(By.XPATH, "//a[@href='projects/6768b820cbf3d7cefd38875d']")
    projects_link.click()
    time.sleep(2)  # Wait for the project page to load

    # Step 6: Click on the delete icon for a resource
    delete_icon = driver.find_element(By.XPATH, "//button[contains(@class, 'bg-rose-500')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", delete_icon)  # Scroll to the delete icon
    delete_icon.click()
    time.sleep(2)  # Wait for the modal to appear

    # Step 7: Verify the modal title
    modal_title = driver.find_element(By.XPATH, "//h1[contains(text(), 'Delete resource')]")
    if modal_title.is_displayed():
        print("Test Passed: Modal title 'Delete resource' is displayed.")
    else:
        print("Test Failed: Modal title not found.")

    # Step 8: Click the delete button in the modal
    try:
        delete_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'bg-rose-500') and text()='Delete']")
            )
        )
        delete_button.click()
        print("Test Passed: Delete button clicked successfully.")
    except Exception as e:
        print(f"Test Failed: Delete button not found or not clickable. Error: {e}")

    # Optional Step 9: Verify the resource is deleted
    # This step depends on how the application reflects the deletion, such as a success message or updated list
    time.sleep(3)  # Allow some time for the page to reflect the deletion

    driver.save_screenshot("Resource_Deleted.png")

finally:
    # Close the browser
    driver.quit()
