import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
token = '4affa205b91011077ac9bbb992f45692'
header = {'Content-Type' : 'application/json', 'trainer_token' : token}
trainer_id = '6880'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : trainer_id}, headers = header)
    assert response.status_code == 200

def test_name_trainer():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : trainer_id}, headers = header)
    assert response_get.json()["data"][0]["id"] == '6880'

