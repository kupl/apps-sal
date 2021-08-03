def cookie(x):
    if isinstance(x, str):
        return 'Who ate the last cookie? It was Zach!'
    elif type(x) in (int, float):
        return 'Who ate the last cookie? It was Monica!'
    else:
        return 'Who ate the last cookie? It was the dog!'
