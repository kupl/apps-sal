def min_value(d):
    L = []
    for i in d:
        if i not in L:
            L.append(i)
    L.sort()
    L1 = []
    for i in L:
        L1.append(str(i))
    return int("".join(L1))
