def cookie(x):
    return f"Who ate the last cookie? It was {('Zach' if type(x) is str else 'Monica' if type(x) in [float, int] else 'the dog')}!"
