import csv
from cadpessoas.models import Pessoas

# Abre o CSV e itera por cada linha
with open("cadastro_pessoas.csv", newline="", encoding="utf-8") as csvfile:
    arquivo = csv.DictReader(csvfile)
    for linha in arquivo:
        Pessoas.objects.create(
            nome=linha['nome'],
            email=linha['email'],
            telefone=linha['telefone'],
            cidade=linha['cidade']
        )

print("Importação concluída com sucesso!")

