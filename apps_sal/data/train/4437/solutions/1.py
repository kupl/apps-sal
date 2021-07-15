def cookie(x):
    try:
        who = {int: 'Monica', float: 'Monica', str: 'Zach'}[type(x)]
    except KeyError:
        who = 'the dog'
    return 'Who ate the last cookie? It was %s!' % who
