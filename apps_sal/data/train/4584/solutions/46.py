def invert(lst):
    x = len(lst)
    for i in range(x):
        lst[i] = lst[i] * -1
    return lst
