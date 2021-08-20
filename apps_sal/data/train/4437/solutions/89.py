def cookie(x):
    if type(x) == str:
        return 'Who ate the last cookie? It was Zach!'
    if type(x) == float or type(x) == int:
        return 'Who ate the last cookie? It was Monica!'
    if type(x) == bool:
        return 'Who ate the last cookie? It was the dog!'
    else:
        return f'Who ate the last cookie? It was {x}!'
