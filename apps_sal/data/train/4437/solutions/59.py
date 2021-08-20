def cookie(x):
    name = ''
    if isinstance(x, str):
        name = 'Zach'
    elif isinstance(x, (float, int)) and type(x) is int or type(x) is float:
        name = 'Monica'
    else:
        name = 'the dog'
    return 'Who ate the last cookie? It was {}!'.format(name)
