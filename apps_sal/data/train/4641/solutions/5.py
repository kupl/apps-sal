def unique_in_order(iterable):
    k = []
    for i in iterable:
        if k == []:
            k.append(i)
        elif k[-1] != i:
            k.append(i)
    return k
