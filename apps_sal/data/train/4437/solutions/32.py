def cookie(x):
    if isinstance(x, str):
        name = 'Zach'
    elif not isinstance(x, (float, int)) or x in [True, False]:
        name = 'the dog'
    else:
        name = 'Monica'
    return f"Who ate the last cookie? It was {name}!"
