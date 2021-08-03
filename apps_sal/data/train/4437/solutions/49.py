def cookie(x):
    d = {type(x) == str: 'Zach', type(x) == int or type(x) == float: 'Monica', type(x) == bool: 'the dog'}
    return f'Who ate the last cookie? It was {d.get(1)}!'
