def cookie(x):
    culprit = ''
    if isinstance(x, str):
        culprit = 'Zach'

    elif isinstance(x, float):
        culprit = 'Monica'

    elif x == 26:
        culprit = 'Monica'

    else:
        culprit = 'the dog'

    return f'Who ate the last cookie? It was {culprit}!'
