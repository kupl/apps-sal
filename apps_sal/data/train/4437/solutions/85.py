def cookie(x):
    if type(x) is float or type(x) is int:
        return "Who ate the last cookie? It was Monica!"
    if isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
    return "Who ate the last cookie? It was the dog!"
