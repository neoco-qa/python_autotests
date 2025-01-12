import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '841647e4d5b16bf8a4982c57e9ea661b'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN }

body_create = {
    "name": "Kapibarich",
    "photo_id": -1
}



response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(" ")
print("Создаем покемона ___")
print(response_create.text)

pokemon_id = response_create.json()['id']

body_rename = {
    "pokemon_id": pokemon_id,
    "name": "Kapipoor",
    "photo_id": 22
}

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename )
print(" ")
print(" ")
print("Капибара меняет имя")
print(response_rename.text)

body_pokeball = {
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball )
print(" ")
print(" ")
print("Капибара в покеболл!")
print(response_pokeball.text)
print(" ")
