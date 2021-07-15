def cookie(x):
    #Good Luck
    if type(x) is str:
        return "Who ate the last cookie? It was Zach!"
    elif isinstance(x, float):
        return "Who ate the last cookie? It was Monica!"
    if type(x) is int:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"
