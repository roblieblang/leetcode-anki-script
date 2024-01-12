import requests
from bs4 import BeautifulSoup
import logging
from termcolor import colored


def scrape_grind75():
    url = (
        "https://www.techinterviewhandbook.org/grind75?hours="
        "15&weeks=20&grouping=topics&mode=all"
    )

    problem_dict = {}
    print(colored("Scraping Grind 75...", "blue"))
    try:
        response = requests.get(url)
        # Raises HTTPError if request returns unsuccessful status code
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP Error: {e}")
        exit()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL: {e}")
        exit()

    html = response.text
    try:
        soup = BeautifulSoup(html, "html.parser")
        for link in soup.find_all("a", href=True):
            if "/problems" in link["href"]:
                problem_link = link["href"]
                problem_name = link.text
                problem_dict[problem_name] = problem_link

    except Exception as e:
        logging.error(f"Error while parsing HTML: {e}")
        exit()

    if len(problem_dict) == 0:
        logging.error(f"No links were scraped from the target url: {url}")
        exit()

    print(
        colored(
            f"Successfully scraped {len(problem_dict)} Grind 75 problems.",
            "green"
        )
    )
    return problem_dict
