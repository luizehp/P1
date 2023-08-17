import json


def extract_route(req):
    route = req.split("/n")[0]
    route = route.split(" ")[1][1::]
    return route

def read_file (path):
    file=open(path,mode="rb")
    return file.read()

def load_data(aq):
    with open("data/"+aq,mode="r") as file:
        a = json.load(file)
    return a

def load_template(aq):
    with open("templates/"+aq,mode="r") as file:
        a = file.read()
    return a