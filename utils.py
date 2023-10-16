import json
from pathlib import Path
from database import database 


def extract_route(req):
    return req.split()[1][1:]

""" def change_route(req):
    delete = req.split()[1][1:]

    request = req.replace(delete, "")
   
    return request """

def read_file(path):
    file = open(path, mode = 'rb')
    return file.read()

def load_data(file):
    caminho = Path() / 'data' / file
    with open(caminho, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def load_template(file):
    caminho = Path() / 'templates' / file
    with open(caminho, 'r', encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    return conteudo

def add_in_file(dic):
    db = database.Database('GETIT')
    """ caminho = Path() / 'data' / 'notes.json'
    with open(caminho,'r') as r:
        data = json.load(r)
    data.append(dic) """
    db.add(database.Note(title=dic['titulo'],content=dic['detalhes']))

    """ with open(caminho, 'w') as f:
        json.dump(data,f) """

def build_response(body='', code=200, reason='OK', headers=''):
    httpv = 'HTTP/1.1'
    response = httpv+' '+str(code)+' '+reason+'\n\n'+body
    if len(headers)>0:
        response = httpv+' '+str(code)+' '+reason+'\n'+headers+'\n\n'+body
    return response.encode()