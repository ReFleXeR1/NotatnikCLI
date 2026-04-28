import pytest
import os
from src.notes_manager import NotesManager

def test_add_note():
    db = "data/test.db"
    manager = NotesManager(db)
    manager.add_note("Test", "Treść testowa", "Kat", "Tag")
    notes = manager.get_all_notes()
    assert len(notes) == 1
    assert notes[0][1] == "Test"
    if os.path.exists(db):
        os.remove(db)