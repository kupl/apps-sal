def cookie(x):
    if isinstance(x,bool):
        name='the dog'
    elif isinstance(x,int) or isinstance(x,float):
        name='Monica'
    elif isinstance(x,str):
        name='Zach'
    return    f"Who ate the last cookie? It was {name}!"
