def cookie(x):
    if (isinstance(x, int) or isinstance(x, float)) and not isinstance(x, bool):
        return "Who ate the last cookie? It was Monica!"
    elif isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
    else:
        return "Who ate the last cookie? It was the dog!"
