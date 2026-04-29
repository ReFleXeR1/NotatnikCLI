import argparse
import sys
import os

# Dodajemy katalog nadrzędny do ścieżki, aby importy działały poprawnie
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import List, Any
from src.notes_manager import NotesManager
from src.utils import check_auth, log_action

def display_notes(notes: List[Any]) -> None:
    """Wyświetla listę notatek w formacie tabelarycznym."""
    if not notes:
        print("Lista notatek jest pusta.")
        return

    header = f"{'ID':<4} | {'Tytuł':<20} | {'Kategoria':<15}"
    print(header)
    print("-" * len(header))

    for note in notes:
        try:
            print(f"{note[0]:<4} | {note[1]:<20} | {note[3]:<15}")
            print(f"Treść: {note[2]}")
            print("-" * len(header))
        except (IndexError, TypeError):
            print("Błąd: Nieprawidłowy format danych notatki.")

def main() -> None:
    if not check_auth():
        print("Błąd autoryzacji. Brak dostępu.")
        sys.exit(1)

    manager = NotesManager()
    
    parser = argparse.ArgumentParser(
        description="Notatnik CLI - System zarządzania notatkami",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Dostępne komendy")

    # Komenda ADD
    add_parser = subparsers.add_parser("add", help="Dodaj nową notatkę")
    add_parser.add_argument("-t", "--title", required=True, help="Tytuł notatki")
    add_parser.add_argument("-c", "--content", required=True, help="Treść notatki")
    add_parser.add_argument("--cat", default="Ogólne", help="Kategoria (domyślnie: Ogólne)")
    add_parser.add_argument("--tags", default="", help="Tagi oddzielone przecinkami")

    # Komenda LIST
    subparsers.add_parser("list", help="Wyświetl wszystkie notatki")

    args = parser.parse_args()

    try:
        if args.command == "add":
            manager.add_note(args.title, args.content, args.cat, args.tags)
            log_action(f"Akcja: Dodawanie | Tytuł: {args.title}")
            print(f"Notatka '{args.title}' została zapisana.")

        elif args.command == "list":
            notes = manager.get_all_notes()
            display_notes(notes)

        else:
            parser.print_help()

    except Exception as error:
        print(f"Krytyczny błąd aplikacji: {error}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram został przerwany przez użytkownika.")
        sys.exit(0)