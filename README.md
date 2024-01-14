## About

Inspired by this [Reddit post](https://www.reddit.com/r/leetcode/comments/ywm91m/using_anki_and_spaced_repetition_with_leetcode/), I made a simple script to scrape LeetCode problem links from some of the most popular problem sets and add them to an Anki deck. Anki serves as a scheduler for this stuyd strategy, deciding for the user when to revisit problems based on their perceived difficulty.

There are thousands of LeetCode problems available to solve, but these curated lists are commonly considered to cover the most fundamental techniques, strategies, patterns, data structures and algorithms.

The purpose of this tool is not to memorize exact LeetCode problems, but instead to devote most of one's study time to weak areas, while also tracking your progress through Anki's native capabilities.

## Requirements

* [Python](https://www.python.org/downloads/)
* Web driver for your browser (I use [Chrome](https://chromedriver.chromium.org/home))
  * Add it to your PATH, or paste the path to the web driver in between the parentheses of `webdriver.Chrome()` in `config.py`
* [Anki](https://apps.ankiweb.net/)
* [Anki Connect](https://git.foosoft.net/alex/anki-connect)

## Getting Started

* Clone the repo to your machine
* Create a new Python virtual environment and activate it
* Create a `.env` following the `.env.example` in the root directory of the project
* Start Anki (it must be running in order for the script to work)
* Run the script with `python main.py` from a CLI in the root directory of the project

## Example Ouput

![example output](https://github.com/roblieblang/leetcode-anki-script/blob/main/images/output1.png?raw=true)
![example output](https://github.com/roblieblang/leetcode-anki-script/blob/main/images/output2.png?raw=true)

## Troubleshooting

- Duplicate Anki Cards Error
  - Delete the deck containing the duplicates and try again
- OSError upon finishing script execution
  - Comment out `time.sleep(0.1)` on line 798 of `venv\Lib\site-packages\undetected_chromedriver\__init__.py`

## Disclaimer

I am not responsible for any misuse of this script. Please respect the websites and their terms.
