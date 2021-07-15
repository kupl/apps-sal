def cookie(x):
    WHO = {str: 'Zach', float: 'Monica', int: 'Monica'}
    return 'Who ate the last cookie? It was {}!'.format(WHO.get(type(x), 'the dog'))
