def invert(lst):
    for ind, elem in enumerate(lst):
        lst[ind] = elem * (-1)
    return lst
