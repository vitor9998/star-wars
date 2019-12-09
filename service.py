import json
import requests 
import unicodedata

class Filmes:
    def filtro(nome):
        nome = str(nome.replace(" ", "-"))

        base_url = 'https://swapi.co/api/people/?search='
        URL = (base_url + nome)
        
        resposta = requests.get(URL)
        lista_de_filmes = resposta.text
        joson_retorno = json.loads(lista_de_filmes)

       


        A=[]
        
        for OBJETO in joson_retorno ['results']:
            B={}
            B['nome'] = OBJETO['name']
            B['altura'] = OBJETO['height']
            B['peso'] = OBJETO['mass']
            B['cor_do_cabelo'] = OBJETO['hair_color']
            B['cor_da_pele'] = OBJETO['skin_color']
            B['cor_do_olho'] = OBJETO['eye_color']
            B['data_nascimento'] = OBJETO['birth_year']
            B['sexo'] = OBJETO['gender']
            B['filmes'] = OBJETO['films']
            B['veículo'] = OBJETO['species']
            B['nave'] = OBJETO['starships']
            B['criação'] = OBJETO['species']
            B['editado'] = OBJETO['edited']
            
            
            A.append(B)
            

        return A
