def invert(lst):
    if lst == []:
        return []
    for i in range(len(lst)):
        lst[i] = -lst[i]
    return lst
