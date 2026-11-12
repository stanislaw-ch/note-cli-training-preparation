import argparse
import hashlib
from pathlib import Path

NOTES_DIR = Path(".notes/db")


def add_note(text):
    content = text.encode("utf-8")
    note_hash = hashlib.sha256(content).hexdigest()

    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    (NOTES_DIR / note_hash).write_bytes(content)
    print(note_hash)

def delete_note(note_hash):
    if len(note_hash) != 64 or any(c not in "0123456789abcdef" for c in note_hash):
        raise SystemExit("Invalid note hash")

    try:
        (NOTES_DIR / note_hash).unlink()
    except FileNotFoundError:
        raise SystemExit("Note not found")

    print(f"Deleted {note_hash}")

def main():
    parser = argparse.ArgumentParser(prog="note")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="Save a note")
    add.add_argument("text")

    delete = commands.add_parser("delete", help="Delete a note")
    delete.add_argument("note_hash")

    args = parser.parse_args()
    if args.command == "add":
        add_note(args.text)
    elif args.command == "delete":
        delete_note(args.note_hash)

if __name__ == "__main__":
    main()