def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    if type(x) in [int, float]:
        return "Who ate the last cookie? It was Monica!"
    return "Who ate the last cookie? It was the dog!"
