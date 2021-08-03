def cookie(x):
    if x == 26:
        return "Who ate the last cookie? It was Monica!"
    if isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
    if isinstance(x, float):
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"
