import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = '4affa205b91011077ac9bbb992f45692'
header = {'Content-Type' : 'application/json', 'trainer_token' : token}
body_creat = {
    "name": "Texmex",
    "photo_id": 325
}
body_transform = {
    "pokemon_id": "127420",
    "name": "Pythonformer",
    "photo_id": 325
}
body_boll = {
    "pokemon_id": "127420"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = header, json = body_creat) # создали покемона
print(response.text)'''

'''response_name = requests.patch(url = f'{URL}/pokemons', headers = header, json = body_transform) # изменил имя  покемона
print(response_name.text)'''

response_boll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = header, json = body_boll) # поймал в покебол
print(response_boll.text)