def cookie(x):
    return f"Who ate the last cookie? It was {('Zach' if isinstance(x, str) else 'the dog' if isinstance(x, bool) else 'Monica' if isinstance(x, int) or isinstance(x, float) else 'the dog')}!"
