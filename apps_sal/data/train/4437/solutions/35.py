def cookie(x):
    name = ""
    if x is str(x):
        name = "Zach!"
    elif x is float(x) or x is int(x):
        name = "Monica!"
    else:
        name = "the dog!"

    return f"Who ate the last cookie? It was {name}"
