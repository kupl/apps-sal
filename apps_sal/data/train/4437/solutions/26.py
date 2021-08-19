def cookie(x):
    # Good Luck
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"

    elif type(x) == int:
        return "Who ate the last cookie? It was Monica!"

    elif type(x) == float:
        return "Who ate the last cookie? It was Monica!"

    else:  # elif type(x) != int or float or str:
        return "Who ate the last cookie? It was the dog!"
