import sqlite3
import os
from datetime import datetime

class NotesManager:
    def __init__(self, db_path="data/notes.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    category TEXT,
                    tags TEXT,
                    created TEXT,
                    updated TEXT
                )
            ''')
    def add_note(self, title, content, category="Ogólne", tags=""):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO notes (title, content, category, tags, created, updated)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (title, content, category, tags, now, now))
a
    def get_all_notes(self):
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute("SELECT * FROM notes").fetchall()        
    
    def search_notes(self, query):
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute(
                "SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?",
                (f"%{query}%", f"%{query}%")
            ).fetchall()
s
    def delete_note(self, note_id):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))