from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from dotenv import load_dotenv
import os
import time

# TODO: CLEANUP EVERYWHERE

# Setup Selenium WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(2)
url = "https://leetcode.com/accounts/login/"
driver.get(url)

# Read LeetCode username and password from .env
load_dotenv(".env")
username = os.environ.get("LEETCODE_USERNAME")
password = os.environ.get("LEETCODE_PASSWORD")

try:
    # Check for properly set username and password
    if not username or not password:
        print("Username or password not set in environment variables.")
        driver.quit()
        exit()
            
    # Wait for page to load first
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.ID, "id_login")
        )
    )
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.ID, "id_password")
        )
    )
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.ID, "signin_btn")
        )
    )
    
    # Log in
    username_field = driver.find_element(By.ID, "id_login") 
    username_field.send_keys(username)
    
    password_field = driver.find_element(By.ID, "id_password")
    password_field.send_keys(password)
    
    login_button = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, "signin_btn"))
    )
    time.sleep(2)
    login_button.click()
    
    print(driver.current_url)
    
    # Click profile icon button
    profile_icon = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.ID, "headlessui-menu-button-5")
        )
    )
    print(driver.current_url)
    profile_icon.click()

    print(driver.current_url)
    # Click List section
    list_section = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/list/']")
        )
    )
    list_section.click()
    
    time.sleep(2)

    # Switch to the new tab
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])

    # Now interact with elements in the new tab
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "mylist-panel"))
    )
    
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "list-group"))
    )
    print(driver.current_url)
    list_items = driver.find_elements(By.CLASS_NAME, "list-group-item")
    print(f"Found {len(list_items)} list items")

    for item in list_items:
        driver.execute_script("arguments[0].scrollIntoView();", item) 
        print(item.text)  

except Exception as e:
    driver.save_screenshot("debug_screenshot.png")  
    print(f"An error occurred: {e}")
    

    # Loop thorugh lists and click on each one
        # class="list-group"
        # class="list-group-item" -> becomes after clicking -> class="list-group-item active"
        # Then we want to extract the questions from each list-group
            # class="list-group-item question"
            # class="question-title" contains an <a> (link) element
                # href="/problems/min-stack/?envType=list&envId=preie3c7" and we want just the /problems/<problem-name>
                # prepended with "https://leetcode.com"
                # the innertext property contains the question name
    # Collect all problems into a set or list and write them to a text file with name and problem link
    
finally:
    driver.quit()
    
