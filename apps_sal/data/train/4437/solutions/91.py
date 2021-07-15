def cookie(x):
    if type(x) == str:
        name = "Zach"
    elif type(x) in [float, int]:
        name = "Monica"
    else:
        name = 'the dog'
    
    
    return f"Who ate the last cookie? It was {name}!"
