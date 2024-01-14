import requests
import random

def load_random_word():
    response = requests.get('https://www.jsonkeeper.com/b/EIG9')
    response_json = response.json()
    word = random.choice(response_json)['word']
    return word

