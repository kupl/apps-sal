def cookie(x):
    if isinstance(x, str):
        return 'Who ate the last cookie? It was Zach!'
    if isinstance(x, bool):
        return 'Who ate the last cookie? It was the dog!'
    if isinstance(x, (float, int)):
        return 'Who ate the last cookie? It was Monica!'
    return 'Who ate the last cookie? It was the dog!'
