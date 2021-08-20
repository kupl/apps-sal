def cookie(x):
    if x == True or x == False:
        return 'Who ate the last cookie? It was the dog!'
    if isinstance(x, int) or isinstance(x, float):
        return 'Who ate the last cookie? It was Monica!'
    if isinstance(x, str):
        return 'Who ate the last cookie? It was Zach!'
    return 'Who ate the last cookie? It was the dog!'
