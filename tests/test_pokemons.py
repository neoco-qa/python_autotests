import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '841647e4d5b16bf8a4982c57e9ea661b'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '16783'

def test_response_status_code():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id': TRAINER_ID} )
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id': TRAINER_ID} )
    assert response.json()['data'][0]['trainer_name'] == 'Капитан Похавал'
