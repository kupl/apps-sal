def cookie(x):
    return "Who ate the last cookie? It was Zach!" if str(x) == x else \
           "Who ate the last cookie? It was Monica!" if isinstance(x, float) or type(x) is int else \
           "Who ate the last cookie? It was the dog!"
