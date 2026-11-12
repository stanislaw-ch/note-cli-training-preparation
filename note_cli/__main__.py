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

def list_notes():
    if not NOTES_DIR.exists():
        return

    for path in sorted(NOTES_DIR.iterdir()):
        if path.is_file():
            print(f"{path.name}  {path.read_text(encoding='utf-8')}")

def main():
    parser = argparse.ArgumentParser(prog="note")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="Save a note")
    add.add_argument("text")
    commands.add_parser("list", help="List saved notes")

    args = parser.parse_args()
    if args.command == "add":
        add_note(args.text)
    elif args.command == "list":
        list_notes()


if __name__ == "__main__":
    main()