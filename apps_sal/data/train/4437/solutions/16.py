def cookie(x):
    name = {isinstance(x, y): z for (z, y) in dict(Zach=str, Monica=(int, float), _dog=bool).items()}.get(1, '_dog').replace('_', 'the ')
    return f'Who ate the last cookie? It was {name}!'
