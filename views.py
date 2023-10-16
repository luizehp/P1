from utils import load_data, load_template
import urllib
from utils import add_in_file, build_response
from database import database
from urllib.parse import unquote

def index(request):

    db = database.Database('GETIT')
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        name=corpo.split("=")[0]
        if name=="titulo":

            for chave_valor in corpo.split('&'):
                o = chave_valor.split('=')
                params[o[0]]=urllib.parse.unquote_plus(o[1])
            add_in_file(params)

        elif name=="id":
            valor=int(corpo.split("=")[1])
            db.delete(valor)

        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')


    """ notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ] """

    notes_li = [
        note_template.format(title=note.title, details=note.content, identificador=note.id)
        for note in db.get_all()
    ]


    notes = '\n'.join(notes_li)

    t =  load_template('index.html').format(notes=notes)
    return build_response(body=t)







def edit(request):

    db = database.Database('GETIT')
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    request = request.replace('\r', '')  # Remove caracteres indesejados
    partes = request.split('\n\n')
    corpo = partes[1]
    name=corpo.split("=")[0]
    if request.startswith('POST'):
        print(name)
        if name == 'id':
            id = corpo.split('=')[1].split('%')[0]
            id = int(id.split("&")[0])
            titulo = corpo.split('titulo=')[1].split('&')[0]
            titulo = unquote(titulo.replace("+", " "))
            descricao = corpo.split('titulo=')[1].split('detalhes=')[1]
            descricao = unquote(descricao.replace("+", " "))

            note = database.Note(id=id,title=titulo,content=descricao)
            db.update(note)

        return build_response(code=303, reason='See Other', headers='Location: /')

    id=partes[0].split("=")[1]
    id=int(id.split(" ")[0])
    note = db.returncard(id)
    note_template = load_template('components/editnote.html').format(title=note.title, content=note.content, identificador=note.id)

    t =  load_template('edit.html').format(editnote=note_template)
    return build_response(body=t)