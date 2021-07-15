def cookie(x):
    print(x)
    if type(x) is str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x) is bool:
        return "Who ate the last cookie? It was the dog!"
    elif type(x) is float or int:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"

