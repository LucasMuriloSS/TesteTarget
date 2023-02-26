import json


with open('./dados.json', 'r') as arquivo:

    dados_json = json.load(arquivo)

dados = dados_json


menor = 0
diamenor = 0
maior = 0
diamaior = 0
soma = 0 
diasmedia = 0

for i in dados:

    soma += i['valor']

    if menor == 0:

        menor = i['valor']

    if i['valor'] < menor and i['valor'] > 0:

        menor = i['valor']
        diamenor = i['dia']

    if i['valor'] > maior:

        maior = i['valor']
        diamaior = i['dia']


media = soma /  len(dados)

for i in dados:

    if i['valor'] > media:

        diasmedia += 1

print(f'o menor valor foi {menor} no dia {diamenor}')
print(f'o Maior valor foi {maior} no dia {diamaior}')
print(f'número de dias em que o faturamento foi maior que a média: {diasmedia}')
        