def cookie(x):
    who = 'the dog'
    if isinstance(x, str):
        who = 'Zach'
    elif isinstance(x, float) or isinstance(x, int):
        who = 'Monica'
    if isinstance(x, bool):
        who = 'the dog'
    return f'Who ate the last cookie? It was {who}!'
