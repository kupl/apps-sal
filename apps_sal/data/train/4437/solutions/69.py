def cookie(x):
    res = isinstance(x, str) 
    nu = isinstance(x, float)
    num = isinstance(x, int)
    if res == True:
        return "Who ate the last cookie? It was Zach!"
    elif x == True or x == False:
        return "Who ate the last cookie? It was the dog!"
    elif nu == True or num == True:
        return "Who ate the last cookie? It was Monica!"

