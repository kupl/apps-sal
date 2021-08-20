def cookie(x):
    name = 'Zach' if isinstance(x, str) else 'Monica' if (isinstance(x, float) or isinstance(x, int)) and (not isinstance(x, bool)) else 'the dog'
    return f'Who ate the last cookie? It was {name}!'
