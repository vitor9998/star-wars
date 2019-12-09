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
        result_json = joson_retorno['results'][0]

        B={}
        if 'name' in result_json and result_json['name']:
            B['nome'] = result_json['name']
        if 'height' in result_json and result_json['height']:
            B['altura'] = result_json['height']
        if 'hair_color' in result_json and result_json['hair_color']:
            B['cor_do_cabelo'] = result_json['hair_color']
        if 'skin_color' in joson_retorno and result_json['skin_color']:
            B['cor_da_pele'] = result_json ['skin_color']
        if 'eye_color' in joson_retorno and result_json['eye_color']:
            B['cor_do_olho'] = result_json ['eye_color']
        if 'birth_year' in joson_retorno and result_json['birth_year']:
            B['data_nascimento'] = result_json ['birth_year']
        if 'gender' in joson_retorno and result_json['gender']:
            B['genêro'] = result_json ['gender']
        if 'homeworld' in joson_retorno and result_json['homeworld']:
            B['mundo_natal'] = result_json ['homeworld']
        if 'films' in joson_retorno and result_json['films']:
            B['filmes'] = result_json ['films']
        if 'species' in joson_retorno and result_json['species']:
            B['espécies'] = result_json ['species']
        if 'vehicles' in joson_retorno and result_json['vehicles']:
            B['veículos'] = result_json ['vehicles']
        if 'starships' in joson_retorno and result_json['starships']:
            B['nave'] = result_json ['starships']
        if 'created' in joson_retorno and result_json['created']:
            B['criação'] = result_json ['created']
        if 'edited' in joson_retorno and result_json['edited']:
            B['editado'] = result_json ['edited']
        


       


       # A=[]
        
        #for OBJETO in joson_retorno ['results']:
            #B={}
            #B['nome'] = OBJETO['name']
            #B['altura'] = OBJETO['height']
            #B['peso'] = OBJETO['mass']
            #B['cor_do_cabelo'] = OBJETO['hair_color']
            #B['cor_da_pele'] = OBJETO['skin_color']
            #B['cor_do_olho'] = OBJETO['eye_color']
            #B['data_nascimento'] = OBJETO['birth_year']
            #B['sexo'] = OBJETO['gender']
            #B['filmes'] = OBJETO['films']
            #B['veículo'] = OBJETO['species']
            #B['nave'] = OBJETO['starships']
            #B['criação'] = OBJETO['species']
            #B['editado'] = OBJETO['edited']
            
            
            #A.append(B)'''
            

        return B
