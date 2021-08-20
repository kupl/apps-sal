def cookie(x):
    z = 'Zach'
    m = 'Monica'
    d = 'the dog'
    if isinstance(x, str):
        return f'Who ate the last cookie? It was {z}!'
    elif isinstance(x, bool):
        return f'Who ate the last cookie? It was {d}!'
    elif isinstance(x, int) or isinstance(x, float):
        return f'Who ate the last cookie? It was {m}!'
    else:
        return f'Who ate the last cookie? It was {d}!'
