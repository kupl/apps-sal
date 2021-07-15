def cookie(x):
    tp = str(type(x))
    if tp == "<class 'str'>":
        return f'Who ate the last cookie? It was Zach!'
    elif tp == "<class 'float'>" or tp == "<class 'int'>":
        return f'Who ate the last cookie? It was Monica!'
    elif tp == "<class 'bool'>":
        return f'Who ate the last cookie? It was the dog!'
