def cookie(x):
    d = {'str': 'Zach', 'float': 'Monica', 'int': 'Monica'}
    return f"Who ate the last cookie? It was {d.get(type(x).__name__, 'the dog')}!"
