def cookie(x):
    if type(x) in (int, float):
        return 'Who ate the last cookie? It was Monica!'
    elif type(x) == str:
        return 'Who ate the last cookie? It was Zach!'
    return 'Who ate the last cookie? It was the dog!'
