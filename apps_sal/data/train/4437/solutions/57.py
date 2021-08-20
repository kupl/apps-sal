def cookie(x):
    return 'Who ate the last cookie? It was ' + ({str: 'Zach', float: 'Monica', int: 'Monica'}.get(type(x)) if type(x) in [str, float, int] else 'the dog') + '!'
