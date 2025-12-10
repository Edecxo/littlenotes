import json

"""Functions for storing json objects into file."""

default_path = 'data/test.json'

def note_store(note, path=default_path):
    """Adds a new note object at path."""
    with open('data/test.json', 'w'):
        pass

def note_list(path=default_path):
    """Lists all note objects at path."""
    with open('data/test.json', 'r') as file:
        data = json.loads(file.read())
    all_notes = []
    for entry in data:
        all_notes.append(entry)
    return all_notes

def note_retrieve(note_name, path=default_path):
    """Shows a specific note at path."""
    with open('data/test.json', 'r') as file:
        data = json.loads(file.read())
    for entry in data:
        if note_name == entry['id'] or note_name == entry['title']:
            return entry
    return f'"{note_name}" not found.'

def note_delete(note_name, path=default_path):
    """Deletes a specific note at path."""
    pass
