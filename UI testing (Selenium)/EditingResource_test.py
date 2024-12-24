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

    # click on the "Data" button
    data_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Data')]")
    data_button.click()
    time.sleep(2) 

    # clear the textarea using JavaScript and write new content
    textarea = driver.find_element(By.TAG_NAME, "textarea")
    driver.execute_script("arguments[0].value = '';", textarea)
    textarea.send_keys("""
[
  {
    "name": "test"
  }
]
""")
    time.sleep(1) 

    # wait for the "Update" button to appear and click it
    try:
        update_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#overlay > div > div > form > div.grid.grid-cols-2.gap-4.sticky.bottom-0.justify-between.p-4.bg-gray-50.rounded-br-2xl.rounded-bl-2xl.-mx-4 > button.cursor-pointer.bg-blue-500.shadow-blue-500\\/50.hover\\:bg-blue-600.active\\:bg-blue-700.text-white")
            )
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", update_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", update_button) 
        print("Test Passed: Update button clicked successfully.")
        time.sleep(3) 
    except Exception as e:
        print(f"Test Failed: Update button not found or not clickable. Error: {e}")
    # save a screenshot
    driver.save_screenshot("Resource_Edited.png")
        
finally:
    driver.quit()
