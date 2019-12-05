import json
import requests 
import unicodedata

class Filmes:
    
    def filtro(nome):
        nome = nome.replace(" ", "-")
        
        URL = 'https://swapi.co/api/'
       

        
        resposta = requests.get(URL)        #naldo


        lista_de_filmes = resposta.text
        

    
       
       

    

        return lista_de_filmes


        


        
       