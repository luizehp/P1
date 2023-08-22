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