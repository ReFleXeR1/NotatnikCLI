import argparse
import sys
from notes_manager import NotesManager
from utils import check_auth, log_action

def main():
    if not check_auth():
        sys.exit()

    manager = NotesManager()
    parser = argparse.ArgumentParser(description="Notatnik CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Dodaj notatkę
    add_p = subparsers.add_parser("add", help="Dodaj nową notatkę")
    add_p.add_argument("--title", required=True, help="Tytuł notatki")
    add_p.add_argument("--content", required=True, help="Treść notatki")
    add_p.add_argument("--cat", default="Ogólne", help="Kategoria")
    add_p.add_argument("--tags", default="", help="Tagi")

    # Lista notatek
    subparsers.add_parser("list", help="Pokaż wszystkie notatki")

    args = parser.parse_args()

    if args.command == "add":
        manager.add_note(args.title, args.content, args.cat, args.tags)
        log_action(f"Dodano notatkę: {args.title}")
        print("Notatka została zapisana.")

    elif args.command == "list":
        notes = manager.get_all_notes()
        for n in notes:
            print(f"ID: {n[0]} | Tytuł: {n[1]} | Kategoria: {n[3]}")
            print(f"Treść: {n[2]}\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()