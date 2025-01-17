import requests

headers = {'Authorization': 'Token 30bb876c2947591d39c4210400172c54e10b0943'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

#curso = requests.get(url=f'{url_base_cursos}3/', headers=headers)
#print(curso.json())

resultado = requests.delete(url=f'{url_base_cursos}3/', headers=headers)
assert resultado.status_code == 204
assert len(resultado.text) == 0