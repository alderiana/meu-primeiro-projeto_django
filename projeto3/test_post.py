import requests

url = 'http://localhost:8000/api/autores/'
token = '60349d2ea88e5bb0e3b182575b7176e2c532dfa1'

data = {
    'nome': 'Jô Soares'
}

headers = {
    'Authorization': f'Token {token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 201:
    print('Autor criado com sucesso:', response.json())
else:
    print('Erro ao criar autor:', response.status_code, response.text)
