def invert(lst):
    for i in range(0, len(lst)):
        if lst[i] >= 0:
            lst[i] = 0 - lst[i]
        else:
            lst[i] = 0 + abs(lst[i])
    return lst
