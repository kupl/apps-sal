def cookie(x):    
    if isinstance(x, bool):
        name = 'the dog'
    elif isinstance(x,str):
        name = 'Zach'         
    else:
        name = 'Monica'
    return "Who ate the last cookie? It was {}!".format(name)
