from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dotenv import load_dotenv
import os
import time
import config
import logging
from termcolor import colored


def login_to_leetcode(driver, username, password):
    # Wait for page to load
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "id_login")))
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "id_password")))
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "signin_btn")))

    # Log in
    username_field = driver.find_element(By.ID, "id_login")
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, "id_password")
    password_field.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, "signin_btn")))
    time.sleep(2)  # Consider using a more reliable wait here
    login_button.click()
    

def navigate_to_profile(driver):
    profile_icon = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.ID, "headlessui-menu-button-5")))
    profile_icon.click()

    list_section = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='/list/']")))
    list_section.click()

    # Switch to the new tab
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
    
    
def extract_problems_from_list(driver):
    problem_dict = {}
    
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, "mylist-panel")))

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, "list-group")))
    
    list_items = driver.find_elements(
        By.CSS_SELECTOR, ".list-group-item:not(.session-select)")

    for item in list_items:
        driver.execute_script("arguments[0].scrollIntoView();", item)
        item.click()
        
        # Find all problems for the current list
        problems = driver.find_elements(By.CSS_SELECTOR, ".question-title a")
        
        for problem in problems:
            # Extract the question link and title
            problem_link = problem.get_attribute("href").split("?")[0]
            problem_name = problem.get_attribute("innerText").strip()
            problem_dict[problem_name] = problem_link

    return problem_dict


# Driver function
def scrape_leetcode():    
    config.setup_logging()

    driver = config.get_webdriver(headless=False)
    url = "https://leetcode.com/accounts/login/"

    # Read LeetCode username and password from .env
    load_dotenv(".env")
    username = os.environ.get("LEETCODE_USERNAME")
    password = os.environ.get("LEETCODE_PASSWORD")
    
    print(colored("Scraping LeetCode...", "blue"))
    try:
        # Check for properly set username and password
        if not username or not password:
            logging.error(
                "Username and/or password not set in environment variables."
            )
            return {}

        driver.get(url)
        login_to_leetcode(driver, username, password)
        navigate_to_profile(driver)
        problem_dict = extract_problems_from_list(driver)
                
    except NoSuchElementException:
        logging.error("Element not found.")
    except TimeoutException:
        logging.error("Request timed out.")

    finally:
        driver.quit()
    
    print(
        colored(
            f"Successfully scraped {len(problem_dict)} LeetCode problems.",
            "green"
        )
    )
    return problem_dict


if __name__ == "__main__":
    scrape_leetcode()