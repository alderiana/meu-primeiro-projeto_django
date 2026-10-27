import requests

url = 'http://localhost:8000/api/autores/'

response = requests.get(url)

if response.status_code == 200:
    autores = response.json()
    for autor in autores:
        print(f"ID: {autor['id']}, Nome: {autor['nome']}")
else:
    print(f"Erro: {response.status_code}")
