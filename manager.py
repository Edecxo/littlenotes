import storage
import datetime

'''
Functions for converting data into json format as specified below.


================
Note json format
================

{
    'id: [id],
    'title': [title],
    'body': [body],
    'timestamp': {
        'created': [created_timestamp],
        'updated': [updated_timestamp]
    }
}
'''


def note_format(title, body):
    '''
    Formats the note into json.
    Refer to docstring at the beginning of this file.
    '''
    new_id = str(1)
    existing_ids = [note['id'] for note in storage.note_list()]
    while new_id in existing_ids:
        new_id = str(int(new_id) + 1)

    dt = datetime.datetime.now()
    now = datetime.datetime.strftime(dt, "%b %d %Y %H:%M")

    new_note = {
            'id': new_id,
            'title': title,
            'body': body,
            'timestamp': {
                'created': now,
                'updated': now
            }
    }
    return new_note
