def cookie(x):
    name = 'Zach' if type(x) == str else 'Monica' if type(x) in (int, float) else 'the dog'
    return "Who ate the last cookie? It was {}!".format(name)
