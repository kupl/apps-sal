def cookie(x):
    if isinstance(x, str):
        name = "Zach"
    elif x ==True or x==False:
        name = "the dog"
    elif isinstance(x, (float,int)):
        name = "Monica"
    
    else:
        name = "the dog"    
    return f"Who ate the last cookie? It was {name}!"
