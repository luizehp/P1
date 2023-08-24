import json
from pathlib import Path


def extract_route(req):
    #route = req.split("\n")[0]
    #print(route)
    #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    #route = route.split(" ")[1][1::]
    return req.split()[1][1:]

def read_file (path):
    file=open(path,mode="rb")
    return file.read()

def load_data(file):
    c=Path() / 'data' / file
    with open(c,"r") as aq:
        a = json.load(aq)
    return a

def load_template(file):
    c=Path() / 'templates' / file
    with open(c,"r") as aq:
        a = aq.read()
    return a

def add_in_file(dic):
    caminho = Path() / 'data' / 'notes.json'
    with open(caminho,'r') as r:
        data = json.load(r)
    data.append(dic)
    with open(caminho, 'w') as f:
        json.dump(data,f)

def build_response(body='', code=200, reason='OK', headers=''):
    httpv = 'HTTP/1.1'
    response = httpv+' '+str(code)+' '+reason+'\n\n'+body
    if len(headers)>0:
        response = httpv+' '+str(code)+' '+reason+'\n'+headers+'\n\n'+body
    return response.encode()