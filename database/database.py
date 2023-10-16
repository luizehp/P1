import sqlite3
from dataclasses import dataclass

class Database:
    def __init__(self, database):
        self.conn = sqlite3.connect(database + ".db")
        self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);")
    
    def add(self, note):
        self.conn.execute(f"INSERT INTO note (title,content) VALUES ('{note.title}', '{note.content}');")
        self.conn.commit()
    
    def get_all(self):
        lista=[]
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            lista.append(Note(id,title,content))
        return lista

    def update(self, entry) -> None:
        self.conn.execute("UPDATE note SET title = ?, content = ?  WHERE id = ?", (entry.title, entry.content, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = {note_id}")
        self.conn.commit()
    
    def returncard(self, id):
        notes=self.get_all()
        for i in notes:
            if i.id==id:
                note=i
        return note
    
    

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''