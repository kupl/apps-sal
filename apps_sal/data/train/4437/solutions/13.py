def cookie(x):
    if type(x) == str:
        x = 'Zach'
    elif type(x) == int or type(x) == float:
        x = 'Monica'
    else:
        x = 'the dog'
    return f'Who ate the last cookie? It was {x}!'
