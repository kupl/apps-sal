def cookie(x):
    if type(x) == type('x'):
        name = 'Zach'
    elif type(x) == type(42) or type(x) == type(3.14):
        name = 'Monica'
    else:
        name = 'the dog'
    return 'Who ate the last cookie? It was %s!' % name
