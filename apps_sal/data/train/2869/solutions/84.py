def distinct(seq):
    dct = {}
    lst = list()
    for i in seq:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] = dct[i] + 1
    for j in dct.keys():
        lst.append(j)
    return lst
