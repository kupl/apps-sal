def cookie(x):
    types = {
        'str': 'Zach',
        'int': 'Monica',
        'float': 'Monica'
    }

    return 'Who ate the last cookie? It was {0}!'.format(
        types.get(type(x).__name__, 'the dog'))
