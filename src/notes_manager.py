import sqlite3
import os
from datetime import datetime
from typing import List, Tuple, Any

class NotesManager:
    def __init__(self, db_path: str = "data/notes.db"):
        """Inicjalizuje menedżera notatek i tworzy bazę danych, jeśli nie istnieje."""
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self) -> None:
        """Tworzy strukturę tabeli dla notatek."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL,
                        category TEXT,
                        tags TEXT,
                        created TEXT,
                        updated TEXT
                    )
                """)
        except sqlite3.Error as e:
            print(f"Błąd inicjalizacji bazy danych: {e}")

    def add_note(self, title: str, content: str, category: str = "Ogólne", tags: str = "") -> None:
        """Dodaje nową notatkę do bazy."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    INSERT INTO notes (title, content, category, tags, created, updated)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (title, content, category, tags, now, now))
        except sqlite3.Error as e:
            print(f"Błąd podczas dodawania notatki: {e}")

    def get_all_notes(self) -> List[Tuple[Any, ...]]:
        """Pobiera wszystkie notatki z bazy."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                return conn.execute("SELECT * FROM notes").fetchall()
        except sqlite3.Error as e:
            print(f"Błąd podczas pobierania notatek: {e}")
            return []

    def delete_note(self, note_id: int) -> bool:
        """Usuwa notatkę na podstawie ID."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Błąd podczas usuwania: {e}")
            return False