def cookie(x):
    if x == True or x == False:
        return 'Who ate the last cookie? It was the dog!'
    if isinstance(x, (int, float)):
        return 'Who ate the last cookie? It was Monica!'
    elif isinstance(x, str):
        return 'Who ate the last cookie? It was Zach!'
    else:
        return 'Who ate the last cookie? It was the dog!'
