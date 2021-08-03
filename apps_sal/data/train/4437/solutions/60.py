def cookie(x):
    if type(x) is str:
        busted = "Zach"
    elif type(x) in (int, float):
        busted = "Monica"
    else:
        busted = "the dog"
    return f"Who ate the last cookie? It was {busted}!"
