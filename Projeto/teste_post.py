import requests

headers = {'Authorization': 'Token 30bb876c2947591d39c4210400172c54e10b0943'} #6a192de3bb41380ba44d477ecce73d377ebfba1a
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "testeUBsocial_Pelotas",
    "url": "http://testeUBsocial04.com"
}
resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Imprime o corpo da resposta como texto
print("Resposta como texto:")
print(resultado.text)

# Imprime o corpo da resposta como JSON
print("Resposta como JSON:")
try:
    print(resultado.json())
except ValueError:
    print("A resposta não está no formato JSON.")

assert resultado.status_code == 201 #Se houve código 201 na Response
assert resultado.json()['titulo'] == novo_curso['titulo'] #Se Response retornará com mesmo informado para criar