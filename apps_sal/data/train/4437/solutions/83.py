def cookie(x):
    culprit = 'the dog'
    if type(x) == type(''):
        culprit = 'Zach'
    elif type(x) == type(1) or type(x) == type(1.1):
        culprit = 'Monica'
    return 'Who ate the last cookie? It was {0}!'.format(culprit)
