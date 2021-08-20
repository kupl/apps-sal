def cookie(x):
    return 'Who ate the last cookie? It was Zach!' if type(x) == str else 'Who ate the last cookie? It was Monica!' if type(x) == int or type(x) == float else 'Who ate the last cookie? It was the dog!'
