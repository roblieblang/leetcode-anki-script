"""
Card Structure:
* anki supports html *
Front:
    f"<a href={problem_link}>{problem_name}</a>"
Back (or maybe all of this should go on the front?):
    <h2>Instructions:</h2>
        - Click on problem link and try to solve the problem
            - Submission accepted: click "Easy" and move on
            - Submission rejected:
                - You're totally clueless: read the solution and bury the Card
                - You failed after trying to code the correct pattern: read the solution and click "Hard"
                - Your solution is almost right, but you missed a small detail: read the solution and click "Good"          
"""

import neetcode_scraper
import leetcode_scraper
import grind75_scraper

from termcolor import colored
import logging


def main():
    all_problems = {}

    try:
        neetcode_problems = neetcode_scraper.scrape_neetcode()
        leetcode_problems = leetcode_scraper.scrape_leetcode()
        grind75_problems = grind75_scraper.scrape_grind75()

        for name, link in neetcode_problems.items():
            all_problems[name] = link

        for name, link in leetcode_problems.items():
            all_problems[name] = link

        for name, link in grind75_problems.items():
            all_problems[name] = link

    except Exception as e:
        logging.error(colored(f"An error occurred: {e}", "red"))

    print(
        colored(
            f"Successfully scraped {len(all_problems)} unique problems:", 
            "magenta", attrs=["bold"]
        )
    )


if __name__ == "__main__":
    main()
