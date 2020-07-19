import requests
from . import apikey

    
def get_word(word: str) -> list:
    r = requests.get(
        f"https://www.dictionaryapi.com/api/v3/references/sd3/json/{word}?key={apikey.apikey}"
    )
    json_response = r.json()[0]
    word = json_response["meta"]["id"]
    definitions = json_response["shortdef"]
    word_info = {"word": word, "definitions": definitions}
    return word_info


if __name__ == "__main__":
    w = input("What word would you like to request? ")
    w_inf = get_word(w)
    formatted_inf = """Word: {word}
Definitions: \n{definitions}""".format(
        word=w_inf["word"],
        offensive=w_inf["offensive"],
        definitions="".join(
            [
                f"   {i+1}: {definition} \n"
                for i, definition in enumerate(w_inf["definitions"])
            ]
        ),
    )
    print(formatted_inf)
