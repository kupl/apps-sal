def cookie(x):
    s = 'Who ate the last cookie? It was '
    if type(x) == str:
        return s + 'Zach!'
    elif type(x) == int or type(x) == float:
        return s + 'Monica!'
    else:
        return s + 'the dog!'
