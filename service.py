import json
import requests 
import unicodedata
from .utilidade import sexo
from .utilidade import cor_do_olho
from .utilidade import cor_da_pele
from .utilidade import tipo_terreno
from .utilidade import cor_do_cabelo
import re
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
            B['cor_do_cabelo'] = cor_do_cabelo(result_json['hair_color'])

        if 'skin_color' in result_json and result_json['skin_color']:
            _corzinha = re.split(',', cor_da_pele(result_json['skin_color']))
            B['cor_da_pele'] = _corzinha
        



           
            
        
            
        if 'eye_color' in result_json and result_json['eye_color']:
            B['cor_do_olho'] = cor_do_olho(result_json['eye_color'])

        if 'birth_year' in result_json and result_json['birth_year']:
            B['data_nascimento'] = result_json['birth_year']

        if 'gender' in result_json and result_json['gender']:
            B['genêro'] = sexo(result_json['gender'])
        

        if'homeworld'in result_json and result_json['homeworld']:
            _mundo_natal = {}
            resposta_mundo_natal = requests.get(result_json['homeworld'])
            mundo_json = json.loads(resposta_mundo_natal.text)
            _mundo_natal['Nome'] = mundo_json['name']
            _mundo_natal['Terreno'] = tipo_terreno(mundo_json['terrain'])
            B['Mundo_Natal'] = _mundo_natal


        if 'films' in result_json and result_json['films']:
            films = []              
            for OBJETO in result_json['films']:
                C = {}
                resposta_filmes = requests.get(OBJETO)
                film_json = json.loads(resposta_filmes.text)
                C['Título'] = film_json['title']
                C['Episódio'] = film_json['episode_id']
                films.append(C)
            B['Filmes'] = films
        



        if 'species' in result_json and result_json['species']:
            especie = []
            for OBJETO2 in result_json['species']:
                D={}
                reposta_epecies = requests.get(OBJETO2)
                especie_json = json.loads(reposta_epecies.text)
                D['Nome'] = especie_json['name']
                D['classificação'] = especie_json['classification']
                D['Língua'] = especie_json['language']
                especie.append(D)
                
            B['espécies'] = especie



        if 'vehicles' in result_json and result_json['vehicles']:
            veiculo = []
            for OBJETO3 in result_json['vehicles']:
                E ={}
                resposta_veiculo = requests.get(OBJETO3)
                veiculo_json = json.loads(resposta_veiculo.text)
                E['Nome'] = veiculo_json['name']
                E['Modelo'] = veiculo_json['model']
                veiculo.append(E)


            B['veículos'] = veiculo


        if 'starships' in result_json and result_json['starships']:
            nave = []
            for OBJETO4 in result_json['starships']:
                F={}
                resposta_nave = requests.get(OBJETO4)
                nave_json = json.loads(resposta_nave.text)
                F['Nome'] = nave_json['name']
                F['Modelo'] = nave_json['model']
                F['Passageiros'] = nave_json['passengers']

                nave.append(F)



            B['nave'] = nave


        if 'created' in result_json and result_json['created']:
            B['criação'] = result_json['created']
        if 'edited' in result_json and result_json['edited']:
            B['editado'] = result_json['edited']
        


       


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
