def cookie(x):
    if type(x) == float or type(x) == int:
        name = "Monica"
    elif type(x) == str:
        name = "Zach"
    else:
        name = "the dog"

    return (f"Who ate the last cookie? It was {name}!")
