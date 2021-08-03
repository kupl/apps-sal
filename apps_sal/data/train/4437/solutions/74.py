def cookie(x):
    return "Who ate the last cookie? It was " + ("Zach!" if isinstance(x, str) else "the dog!" if isinstance(x, bool) else "Monica!")
