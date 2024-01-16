from flask import Flask

app = Flask(__name__)

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

@app.route("/usuarios")
def get_users_by_name():
    params = {
        name: "params.name",
        email: "params.email"
    }
    return usuario
