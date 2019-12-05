from flask import Blueprint, Response, request, jsonify
from service import Filmes
import requests
import json


Lista = Blueprint(
    "pessoa", __name__, url_prefix="/v1/filmes"
)

@Lista.route("/pessoa/<nome>", methods=["GET"])
def Personagem(nome):
    a = Filmes.filtro(nome)
    b = json.dumps(a)   

    return b  
    
