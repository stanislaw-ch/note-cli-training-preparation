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


def main():
    parser = argparse.ArgumentParser(prog="note")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="Save a note")
    add.add_argument("text")

    args = parser.parse_args()
    if args.command == "add":
        add_note(args.text)


if __name__ == "__main__":
    main()