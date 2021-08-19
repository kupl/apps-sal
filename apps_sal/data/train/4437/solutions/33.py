def cookie(x):
    print(x, type(x))
    if isinstance(x, str):
        return 'Who ate the last cookie? It was Zach!'
    elif isinstance(x, (int, float)) and (not isinstance(x, bool)):
        return 'Who ate the last cookie? It was Monica!'
    else:
        return 'Who ate the last cookie? It was the dog!'
