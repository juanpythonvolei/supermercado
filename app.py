from flask import Flask,render_template
from functions.users.functions_users import *
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('app.html',nome='juan')

@app.route('/api/usuarios/<nome>/<email>/<senha>/')
def adicionar_usuario(nome:str,email:str,senha:int):
    try:
        novo_usuario = add_users(nome,email,senha)
        return {'status':f'{novo_usuario}'}
    except:
       session.rollback()
       return {'status':'erro'}
    
@app.route('/api/usuarios/consulta/<email>')    
def consultar_usuario(email:str):
    usuairo = get_user(email)
    if usuairo:
        return {'status':f"{usuairo}"}
    else:
        return {'status':'erro'}
    
@app.route('/api/usuarios/exclusao/<email>')
def apagar_usuario(email:str):
    if delete_user(email):
        return {'status':'Usuario excluido'}
    else:
        return {'status':'erro'}

    
app.run(debug=True)
