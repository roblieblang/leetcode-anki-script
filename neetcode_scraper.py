from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import config
import logging
from termcolor import colored


def scrape_neetcode():
    driver = config.get_webdriver(headless=False)

    url = "https://neetcode.io/practice"
    driver.get(url)

    # {problem_link: problem_name}
    # since there are duplicate names with different casing
    problem_dict = {}
    print(colored("Scraping NeetCode...", "blue"))
    try:
        # Click NeetCode 150 tab
        nc_150_xpath_locator = "//*[contains(text(), '🚀') and \
            contains(text(), 'NeetCode 150')]"
        nc_150_tab = driver.find_element(By.XPATH, nc_150_xpath_locator)
        nc_150_tab.click()

        # Wait for table to load
        # nc_150_table_xpath_locator = (
        #     "//app-pattern-table-list[@class='ng-star-inserted']"
        # )
        # WebDriverWait(driver, 50).until(
        #     expected_conditions.presence_of_element_located(
        #         (By.XPATH, nc_150_table_xpath_locator)
        #     )
        # )
        for element in driver.find_elements(By.CSS_SELECTOR, 
                                            "a.table-text.text-color"):
            problem_name = element.get_attribute("innerText").strip()
            problem_link = element.get_attribute("href").rstrip('/')
            problem_dict[problem_link] = problem_name

    except NoSuchElementException:
        logging.error(colored("Element not found.", "red"))
    except TimeoutException:
        logging.error(colored("Request timed out.", "red"))

    finally:
        driver.quit()

    print(
        colored(f"Successfully scraped {len(problem_dict)} NeetCode problems.", 
                "green")
    )
    return problem_dict


if __name__ == "__main__":
    res = scrape_neetcode()
    for link, name in res.items():
        print(f"{name}: {link}")