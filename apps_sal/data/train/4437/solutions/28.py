def cookie(x):
    name = "Monica" if type(x) == int or type(x) == float else "the dog" if type(x) == bool else "Zach"
    return "Who ate the last cookie? It was {}!".format(name)
