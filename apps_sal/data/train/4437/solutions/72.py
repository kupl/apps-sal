def cookie(x):
    return 'Who ate the last cookie? It was Zach!' if type(x) == str else 'Who ate the last cookie? It was Monica!' if type(x) in [int, float] else 'Who ate the last cookie? It was the dog!'
