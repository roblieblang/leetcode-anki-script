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
import requests
from bs4 import BeautifulSoup

urls = [
    # Grind 75
    "https://www.techinterviewhandbook.org/grind75?hours=15&weeks=20&grouping=topics&mode=all",
    # NeetCode 150
    "https://neetcode.io/practice",
]

url = "https://www.techinterviewhandbook.org/grind75?hours=15&weeks=20&grouping=topics&mode=all"
# url = "https://neetcode.io/practice"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

# TODO: grab the problem names as well as their links
links = []
for link in soup.find_all("a", href=True):
    if "/problems" in link["href"]:
        full_link = link["href"]
        links.append(full_link)

unique_links = set(links)

assert len(links) == 169, \
    f"Some links are missing from target url: {url}"

assert len(links) > 0, \
    f"Some error occurred and no links were scraped from the target url: {url}"


print(f"{len(links)} links found:")
for link in links:
    print("  " + link)
    
with open("grind-75-problems.txt", "w", encoding="utf-8") as file:
    for link in links:
        file.write(link + "\n")
