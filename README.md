## About

Inspired by this [Reddit post](https://www.reddit.com/r/leetcode/comments/ywm91m/using_anki_and_spaced_repetition_with_leetcode/), I made a script to scrape LeetCode problem links from some of the most popular problem sets and add them to an Anki deck. Anki serves as a scheduler for this application, deciding for the user when to revisit problems based on their perceived difficulty.

There are thousands of LeetCode problems available to solve, but these curated lists are commonly considered to cover the most fundamental techniques, strategies, patterns, data structures and algorithms.

The purpose of this tool is not to memorize exact LeetCode problems, but instead to devote most of one's study time to weak areas, while also tracking your progress through Anki's native capabilities. 

Some degree of accountability is afforded by this study strategy as Anki will resurface your weak problems again and again untiul they have become strong.

## Requirements

* Python
* Web driver for your browser (I use [Chrome](https://chromedriver.chromium.org/home))
  * Add it to your PATH, or paste the path into `webdriver.Chrome()` in `<insert filename here>`

## Installation

* Clone the repo to your machine
* Create a `.env` following the `.env.example` in the root directory of the project

## Disclaimer

I am not responsible for any misuse of this script. Please respect the websites, their terms, and their owners.
