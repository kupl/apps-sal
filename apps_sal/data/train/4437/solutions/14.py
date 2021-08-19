def cookie(x):
    return 'Who ate the last cookie? It was {}!'.format({str: 'Zach', float: 'Monica', int: 'Monica'}.get(type(x), 'the dog'))
