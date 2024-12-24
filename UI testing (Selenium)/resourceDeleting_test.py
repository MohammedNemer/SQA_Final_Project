from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

try:
    # open MockAPI website
    driver.get("https://mockapi.io/")
    driver.maximize_window()
    time.sleep(2) 

    # click on the Login button
    login_button = driver.find_element(By.LINK_TEXT, "Login")
    login_button.click()
    time.sleep(2) 

    # enter a valid email and password
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("mohammed-nemer@hotmail.com") 
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("mohammed@2024") 


    # click the Login button
    login_submit_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_submit_button.click()
    time.sleep(3) 

    # click on the "Projects" 
    projects_link = driver.find_element(By.XPATH, "//a[@href='projects/6768b820cbf3d7cefd38875d']")
    projects_link.click()
    time.sleep(2) 

    # click on the delete icon for a resource
    delete_icon = driver.find_element(By.XPATH, "//button[contains(@class, 'bg-rose-500')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", delete_icon)  # Scroll to the delete icon
    delete_icon.click()
    time.sleep(2) 

    # verify the modal title
    modal_title = driver.find_element(By.XPATH, "//h1[contains(text(), 'Delete resource')]")
    if modal_title.is_displayed():
        print("Test Passed: Modal title 'Delete resource' is displayed.")
    else:
        print("Test Failed: Modal title not found.")

    # click the delete button in the modal
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
        
    time.sleep(3)  

    # save a screenshot
    driver.save_screenshot("Resource_Deleted.png")

finally:
    driver.quit()
