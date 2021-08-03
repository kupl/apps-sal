d = {'str': 'Zach', 'int': 'Monica', 'float': 'Monica'}


def cookie(x):
    return f"Who ate the last cookie? It was {d.get(type(x).__name__,'the dog')}!"
