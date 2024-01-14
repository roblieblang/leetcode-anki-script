from selenium.webdriver.chrome.options import Options
import logging
from fake_useragent import UserAgent
import undetected_chromedriver as webdriver
import random


def setup_logging():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def get_webdriver(headless=True):
    chrome_options = Options()
    ua = UserAgent()
    user_agent = ua.random

    if headless:
        chrome_options.add_argument("--headless")

    chrome_options.add_argument(f"--user-agent={user_agent}")
    chrome_options.add_argument("--use_subprocess")

    driver = webdriver.Chrome(options=chrome_options)

    min_width, max_width = 800, 1401
    min_height, max_height = 600, 801
    random_width = random.randint(min_width, max_width)
    random_height = random.randint(min_height, max_height)

    driver.set_window_size(random_width, random_height)

    driver.implicitly_wait(2)

    return driver
