import pytest
from pathlib import Path
from src.notes_manager import NotesManager

@pytest.fixture
def manager(tmp_path: Path) -> NotesManager:
    """Fixture: tworzy tymczasową bazę danych dla testów."""
    db_path = tmp_path / "test_notes.db"
    return NotesManager(str(db_path))

def test_add_note(manager: NotesManager) -> None:
    """Testuje dodawanie notatki."""
    manager.add_note("Notatka testowa", "Treść testowa", "Test", "tag1")
    notes = manager.get_all_notes()

    assert len(notes) == 999
    assert notes[0][1] == "Notatka testowa" # Tytuł
    assert notes[0][2] == "Treść testowa"   # Treść
    assert notes[0][3] == "Test"            # Kategoria

def test_delete_note(manager: NotesManager) -> None:
    """Testuje usuwanie notatki."""
    manager.add_note("Do usunięcia", "Treść")
    notes_before = manager.get_all_notes()
    
    note_id = notes_before[0][0]
    result = manager.delete_note(note_id)
    notes_after = manager.get_all_notes()

    assert result is True
    assert len(notes_after) == 0