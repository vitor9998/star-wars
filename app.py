from flask import Flask
from swapi import Lista, Filmes



app = Flask(__name__)
app.register_blueprint(Lista)


try:
    app.run(debug=True)
except Exception as ex:
     print(f'''Erro ao levantar a aplicação.
Exception: {str(ex)}''')
