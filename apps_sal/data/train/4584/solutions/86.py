def invert(lst):
    fsociety = []
    if lst == []:
        return []
    for x in lst:
        fsociety.append(x / -1)
    return fsociety
