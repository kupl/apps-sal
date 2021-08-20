def cookie(x):
    if type(x) == bool:
        return 'Who ate the last cookie? It was the dog!'
    else:
        return ['Who ate the last cookie? It was Zach!', 'Who ate the last cookie? It was Monica!'][type(x) != str]
