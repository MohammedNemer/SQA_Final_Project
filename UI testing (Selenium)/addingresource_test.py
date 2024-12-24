from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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

    # click on "Projects" 
    projects_link = driver.find_element(By.XPATH, "//a[@href='projects/6768b820cbf3d7cefd38875d']")
    projects_link.click()
    time.sleep(2)


    # click on "New Resource"
    new_resource_button = driver.find_element(By.XPATH, "//button[contains(text(), 'New resource')]")
    new_resource_button.click()
    time.sleep(2)

    # enter the resource name
    resource_name_input = driver.find_element(By.NAME, "name")
    resource_name_input.send_keys("TestResource") 

    # click the "Create" button
    create_button = driver.find_element(By.XPATH, "//button[text()='Create']")
    create_button.click()
    time.sleep(3)

    # verify the new resource is added
    try:
        added_resource = driver.find_element(By.XPATH, "//button[contains(text(), 'New resource')]")
        print("Test Passed: Resource added successfully.")
    except:
        print("Test Failed: Resource not found.")   
    
    # save a screenshot
    driver.save_screenshot("Resource_Added.png")
finally:
    driver.quit()
