import requests

# GET Avaliações:
avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
# print(avaliacoes.status_code)
# print(avaliacoes.json())
# print(avaliacoes.json()['results'][0])


'''
Acessar dados da Response em dicionário Python: print(avaliacoes.json())
Mostrar dados específico (Qtde de itens): print(avaliacoes.json()['count'])
Mostrar dados específico (Próxima página de resultados): print(avaliacoes.json()['next'])

Mostrar resultados da Response: print(avaliacoes.json()['results'])
Mostrar resultado específico da Response: print(avaliacoes.json()['results'][0])
Mostrar dado de resultado específico da Response: print(avaliacoes.json()['results'][0]['nome'])
'''

# GET Avaliação:
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1/')
# print(avaliacao.json())
#print(avaliacao.json()['nome'])

# GET Cursos (Requer autenticação):
headers = {'Authorization': 'Token 30bb876c2947591d39c4210400172c54e10b0943'} #6a192de3bb41380ba44d477ecce73d377ebfba1a
cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
print(cursos.json())