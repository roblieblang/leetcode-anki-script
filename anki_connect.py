import json
import urllib.request
from termcolor import colored
import logging


def request(action, **params):
    return {"action": action, "params": params, "version": 6}


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode("utf-8")
    response = json.load(
        urllib.request.urlopen(
            urllib.request.Request("http://127.0.0.1:8765", requestJson)
        )
    )
    if len(response) != 2:
        raise Exception("Response has an unexpected number of fields")
    if "error" not in response:
        raise Exception("Response is missing required error field")
    if "result" not in response:
        raise Exception("Response is missing required result field")
    if response["error"] is not None:
        raise Exception(response["error"])

    return response["result"]


def create_new_deck(deck_name):
    invoke("createDeck", deck=deck_name)
    print(colored(f"Created new deck '{deck_name}'.", "dark_grey"))
    print(colored(f"All decks: {invoke('deckNames')}", "dark_grey"))


def add_cards_to_deck(deck_name, problems):
    count = 0
    for problem_link, problem_name in problems:
        html_content = f"""
            <div style="text-align: center;">
                <h2>
                    <a href='{problem_link}'>{problem_name}</a>
                </h2>
            </div>
            <div>
                <h4>Instructions</h4>
                <ol>
                    <li>Click problem link and try to solve the problem
                    </li>
                    <li>Submission accepted: click "Easy" and move on</li>
                    <li>
                        Submission rejected:
                        <ul style="list-style-type: lower-alpha;">
                            <li>Totally clueless: 
                                read the solution and bury the Card
                            </li>
                            <li>Failed after trying to 
                                code the correct pattern: 
                                read the solution and click "Hard"
                            </li>
                            <li>Almost there, but not quite: 
                                read the solution and click "Good"
                            </li>
                        </ul>
                    </li>
                </ol>
            </div>
        """
        note = {
            "deckName": deck_name,
            "modelName": "Basic",
            "fields": {
                "Front": html_content,
                "Back": "Done? How did you do?",
            },
            "tags": ["leetcode"],
        }

        response = invoke("addNote", note=note)
        if not response:
            logging.error(
                colored(f"Some error occurred while \
                    adding cards to {deck_name}", "red")
            )
        else:
            print(colored(f"Added card: {problem_name}", "dark_grey"))
            count += 1

    return count


def deck_exists(deck_name):
    existing_decks = invoke("deckNames")
    return deck_name in existing_decks
