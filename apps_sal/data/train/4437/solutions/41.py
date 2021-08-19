def cookie(x):
    # Good Luck
    if isinstance(x, bool):
        return "Who ate the last cookie? It was the dog!"
    if isinstance(x, int) or isinstance(x, float):
        return "Who ate the last cookie? It was Monica!"
    if isinstance(x, str):
        return "Who ate the last cookie? It was Zach!"
    else:
        return "Who ate the last cookie? It was the dog!"
