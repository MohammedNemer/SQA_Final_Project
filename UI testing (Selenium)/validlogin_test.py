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

    # verify successful login by checking the "Projects" element
    try:
        projects_element = driver.find_element(By.XPATH, "//div[contains(text(), 'Projects')]")
        print("Test Passed: Login successful, 'Projects' element found.")
    except:
        print("Test Failed: 'Projects' element not found.")
        
    # save a screenshot
    driver.save_screenshot("Login Success.png")

finally:
   
    driver.quit()
