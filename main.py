import neetcode_scraper
import leetcode_scraper
import grind75_scraper

from anki_connect import create_new_deck, add_cards_to_deck, deck_exists
from config import setup_logging

from termcolor import colored
import logging


def main():
    setup_logging()

    new_deck_name = "LeetCode Mastery"

    if deck_exists(new_deck_name):
        print(
            colored(
                f"Deck '{new_deck_name}' already exists. "
                f"Try a different deck name or "
                f"delete '{new_deck_name}' from Anki.",
                "red",
                attrs=["bold"],
            )
        )
        return

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
        raise e

    print(
        colored(
            f"Successfully scraped {len(all_problems)} unique problems.",
            "magenta",
            attrs=["bold"],
        )
    )

    print(colored(f"Creating a new Anki deck '{new_deck_name}'...", "cyan"))
    create_new_deck(new_deck_name)
    print(colored(f"Adding all problems to '{new_deck_name}' deck...", "cyan"))
    cards = add_cards_to_deck(new_deck_name, all_problems)
    print(
        colored(
            f"{cards} cards added to '{new_deck_name}'.",
            "light_green",
            attrs=["bold", "underline"],
        )
    )


if __name__ == "__main__":
    main()
