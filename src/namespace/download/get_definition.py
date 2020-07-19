import requests
from . import apikey

    
def get_word(word: str) -> list:
    r = requests.get(
        f"https://www.dictionaryapi.com/api/v3/references/sd3/json/{word}?key={apikey.apikey}"
    )
    json_response = r.json()
    if len(json_response) == 0 or 'meta' not in json_response[0]:
        return {'return_type': 'options', 'options': [option for option in r.json()[:min(len(r.json()), 5)]]}
    else:
        word = json_response[0]["meta"]["id"]
        definitions = json_response[0]["shortdef"]
        word_info = {"return_type": "definitions", "word": word, "definitions": definitions}
        return word_info

def get_json(word):
    r = requests.get(
        f"https://www.dictionaryapi.com/api/v3/references/sd3/json/{word}?key={apikey.apikey}"
    )
    json_response = r.json()
    return json_response

if __name__ == "__main__":
    print(get_json(input('What word would you like to request? ')))
