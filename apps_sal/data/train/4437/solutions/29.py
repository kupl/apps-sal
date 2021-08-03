def cookie(x):
    name = {
        'str': 'Zach',
        'int': 'Monica',
        'float': 'Monica',
        'bool': 'the dog',
    }[type(x).__name__]
    return f"Who ate the last cookie? It was {name}!"
