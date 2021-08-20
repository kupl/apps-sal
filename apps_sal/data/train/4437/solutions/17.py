def cookie(x):
    name = dict(zip((isinstance(x, t) for t in (str, (int, float), bool)), ('Zach', 'Monica', 'the dog'))).get(1, 'the dog')
    return f'Who ate the last cookie? It was {name}!'
