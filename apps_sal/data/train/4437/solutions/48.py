def cookie(x):
    return 'Who ate the last cookie? It was %s' % {str: 'Zach', int: 'Monica', float: 'Monica', bool: 'the dog'}.get(type(x)) + '!'
