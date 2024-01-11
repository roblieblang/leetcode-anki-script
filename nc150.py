from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# TODO: run selenium in headless mode once ready for deployment

# TODO: offer option to exclude premium questions(?)

url = "https://neetcode.io/practice"
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get(url)

try:
    # Click NeetCode 150 tab
    nc_150_xpath_locator = (
        "//*[contains(text(), '🚀') and "
        "contains(text(), 'NeetCode 150')]" 
    )
    nc_150_tab = driver.find_element(By.XPATH, nc_150_xpath_locator)
    nc_150_tab.click()
    
    # Wait for table to load
    nc_150_table_xpath_locator = (
        "//app-pattern-table-list[@class='ng-star-inserted']"
    )
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, nc_150_table_xpath_locator)
        )
    )

    # Find all problems in the table
    problem_elements = driver.find_elements(
        By.CSS_SELECTOR, "a.table-text.text-color"
    )
    
    # Write each problem name and link to a file 
    with open("nc-150-problems.txt", "w", encoding="utf-8") as file:
        for element in problem_elements:
            problem_name = element.get_attribute("innerText").strip()
            problem_link = element.get_attribute("href")
            file.write(f"{problem_name}: {problem_link}\n")
    
finally:
    driver.quit()
