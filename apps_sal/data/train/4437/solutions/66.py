def cookie(x):
    name = ''
    if type(x) == str:
        name = 'Zach'
    elif type(x) == float or type(x) == int:
        name = 'Monica'
    else:
        name = 'the dog'
    return 'Who ate the last cookie? It was ' + name + '!'
