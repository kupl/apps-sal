def cookie(x):
    who = "Who ate the last cookie? It was "
    if isinstance(x, bool):
        return who + "the dog!"
    if isinstance(x, str):
        return who + "Zach!"
    if isinstance(x, int) or isinstance(x, float):
        return who + "Monica!"
    return who + "the dog!"
