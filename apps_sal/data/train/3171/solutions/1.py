def crashing_weights(weights):
    lst = [0] * len(weights[0])
    for line in weights:
        lst = [b if a <= b else a+b for a,b in zip(lst, line)]
    return lst
