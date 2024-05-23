import os
import requests

from promptflow import tool

DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')

@tool
def transale(user_input: str) -> str:
    url = 'https://api-free.deepl.com/v2/translate'

    headers = {
        'Authorization': f'DeepL-Auth-Key {DEEPL_API_KEY}',
        'Content-Type': 'application/json'
    }

    json_data = {
        'text': [user_input],
        'source_lang': 'EN',
        'target_lang': 'PL'
    }

    response = requests.post(url=url, headers=headers, json=json_data)

    return response.json()['translations'][0]['text']
