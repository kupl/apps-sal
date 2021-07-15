def cookie(x):
    print(x)
    return "Who ate the last cookie? It was Zach!" if isinstance(x,str)\
            else "Who ate the last cookie? It was Monica!" \
            if (isinstance(x,int) or isinstance(x,float)) and not isinstance(x,bool)\
            else "Who ate the last cookie? It was the dog!"
