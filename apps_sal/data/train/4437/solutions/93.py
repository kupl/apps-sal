def cookie(x):
    name = "Zach" if type(x) == str else "Monica" if type(x) == int or type(x) == float else "the dog"
    result = (f"Who ate the last cookie? It was {name}!")
    return result
