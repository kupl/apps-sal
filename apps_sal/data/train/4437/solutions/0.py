def cookie(x):
    return 'Who ate the last cookie? It was %s!' % {str: 'Zach', float: 'Monica', int: 'Monica'}.get(type(x), 'the dog')
