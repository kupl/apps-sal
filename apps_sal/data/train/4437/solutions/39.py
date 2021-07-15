def cookie(x):    
    if isinstance(x, bool):
        return "Who ate the last cookie? It was the dog!"
    elif isinstance(x,str):
        return  "Who ate the last cookie? It was Zach!"         
    else:
        return "Who ate the last cookie? It was Monica!"
