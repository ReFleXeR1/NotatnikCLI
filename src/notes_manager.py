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
    def add_note(self, title, content, category="Ogolne", tags=""):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO notes (title, content, category, tags, created, updated)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (title, content, category, tags, now, now))

    def get_all_notes(self):
        with sqlite3.connect(self.db_path) as conn:
            return conn.execute("SELECT * FROM notes").fetchall()        