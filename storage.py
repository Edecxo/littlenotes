import json

"""Functions for storing json objects into file."""

def note_store(note, path):
    """Adds a new note object at path."""
    with open('data/test.json', 'w'):
        pass

def note_list(path):
    """Lists all note objects at path."""
    with open('data/test.json', 'r') as file:
        data = json.loads(file.read())
    for entry in data:
        return (f'Note ID: {entry["id"]}\n' +
                f'Title: {entry["title"]}\n'
        )

def note_view(note_name, path):
    """Shows a specific note at path."""
    with open('data/test.json', 'r') as file:
        data = json.loads(file.read())
    for entry in data:
        if note_name == entry['id'] or note_name == entry['title']:
            return (f'Note ID: {entry["id"]}\n' +
                    f'Title: {entry["title"]}\n' +
                    f'Body: {entry["body"]}\n'
            )
    return f'"{note_name}" not found.'

def note_delete(note_name, path):
    """Deletes a specific note at path."""
    pass
