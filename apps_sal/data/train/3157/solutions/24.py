def number(x):
    L = []
    for i in x:
        L.append(i[0])
        L.append(-i[1])
    return sum(L)
