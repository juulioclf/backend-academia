from flask import Flask, request, jsonify
from flask_migrate import Migrate

from dotenv import dotenv_values

from database import db

from diario import Diario

config = dotenv_values(".env")


app = Flask(__name__)

connection = config['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = connection

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello_world():
    return "<p>Hello JULIN, become a friend!</p>"


@app.route("/usuarios")
def get_users():
    usuarios = [  
        {
            "name": "julio ferreira",
            "email": "julio@gmail.com"
        },
        {
            "name": "miguel angelo",
            "email": "miguel@gmail.com"
        }
    ]
    return usuarios

@app.route("/usuarios/1")
def get_users_by_id():
    usuario =  {
            "name": "julio ferreira",
            "email": "julio@gmail.com",
            "apelido": "badmilk",
            "linguagem": "python"
        }
    return usuario

@app.route("/usuarios/name")
def get_users_by_name():
    params = {
        name: "params.name",
        email: "params.email"
    }
    return usuario


#### GALERA REFATORADA
@app.route("/user", methods=['POST'])
def post_user():
   
   payload = request.json

   new_user = Diario(payload['titulo'], payload['disciplina'])

   new_user.post_user(payload['titulo'], payload['disciplina'])

   return payload


@app.route("/user", methods=['GET'])
def post_user():
   
   

   return payload