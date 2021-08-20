def cookie(x):
    result = ''
    if isinstance(x, str):
        result = 'Who ate the last cookie? It was Zach!'
    elif isinstance(x, float) and type(x) is not bool:
        result = 'Who ate the last cookie? It was Monica!'
    elif isinstance(x, int) and type(x) is not bool:
        result = 'Who ate the last cookie? It was Monica!'
    else:
        result = 'Who ate the last cookie? It was the dog!'
    return result
