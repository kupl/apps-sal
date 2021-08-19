def invert(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = -abs(lst[i])
        else:
            lst[i] = abs(lst[i])
    return lst
