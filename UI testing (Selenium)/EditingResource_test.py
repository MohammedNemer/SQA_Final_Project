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

    # Step 6: Click on the "Data" button
    data_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Data')]")
    data_button.click()
    time.sleep(2)  # Wait for the data page to load

    # Step 7: Clear the textarea using JavaScript and write new content
    textarea = driver.find_element(By.TAG_NAME, "textarea")
    driver.execute_script("arguments[0].value = '';", textarea)  # Clear the textarea using JavaScript
    textarea.send_keys("""
[
  {
    "name": "test"
  }
]
""")
    time.sleep(1)  # Wait for the data to populate

    # Step 8: Wait for the "Update" button to appear and click it
    try:
        # Wait for the Update button to be visible and interactable
        update_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#overlay > div > div > form > div.grid.grid-cols-2.gap-4.sticky.bottom-0.justify-between.p-4.bg-gray-50.rounded-br-2xl.rounded-bl-2xl.-mx-4 > button.cursor-pointer.bg-blue-500.shadow-blue-500\\/50.hover\\:bg-blue-600.active\\:bg-blue-700.text-white")
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", update_button)  # Scroll into view
        time.sleep(1)  # Small delay to ensure visibility
        driver.execute_script("arguments[0].click();", update_button)  # Use JavaScript to click the button
        print("Test Passed: Update button clicked successfully.")
        time.sleep(3)  # Wait for the update to process and redirect
    except Exception as e:
        print(f"Test Failed: Update button not found or not clickable. Error: {e}")

    driver.save_screenshot("Resource_Edited.png")
        
finally:
    # Close the browser
    driver.quit()
