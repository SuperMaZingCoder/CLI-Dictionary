import requests
import apikey

def get_word(word: str) -> list:
	r = requests.get(f'https://www.dictionaryapi.com/api/v3/references/sd3/json/{word}?key=your-api-key')