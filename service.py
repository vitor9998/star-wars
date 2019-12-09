import json
import requests 
import unicodedata

class Filmes:
    def filtro(nome):
        nome = str(nome.replace(" ", "-"))
        URL = 'https://swapi.co/api/' + nome
        resposta = requests.get(URL)
        lista_de_filmes = resposta.text
        joson_retorno = json.loads(lista_de_filmes)

        return joson_retorno