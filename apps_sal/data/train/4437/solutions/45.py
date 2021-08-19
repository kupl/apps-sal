def cookie(x):
    who = 'the dog'
    if isinstance(x, str):
        who = 'Zach'
    elif (isinstance(x, float) or isinstance(x, int)) and (not isinstance(x, bool)):
        who = 'Monica'
    return f'Who ate the last cookie? It was {who}!'
