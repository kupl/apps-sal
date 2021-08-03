def cookie(x):
    return 'Who ate the last cookie? It was %s!' % ('Zach' if isinstance(x, str) else
                                                    'Monica' if type(x) == int or isinstance(x, float) else 'the dog')
