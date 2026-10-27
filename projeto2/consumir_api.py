import requests
import json

def consultaAPI():
    # Endereço da sua API que está rodando na janela azul
    url = "http://localhost:8000/pessoas/"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        return []

def formataResposta(user):
    return (
        f"\nID: {user['id']}\n"
        f"Nome: {user['nome']}\n"
        f"E-mail: {user['email']}\n"
        f"Telefone: {user['telefone']}\n"
        f"Cidade: {user['cidade']}\n"
    )

def main():
    users = consultaAPI()
    print("\n=== Lista de Usuários da API (Fixação) ===\n")
    for user in users:
        print(formataResposta(user))
        print("-" * 40)

if __name__ == "__main__":
    main()