def invert(lst):
    lstCopy = lst[:]
    for i in range(len(lst)):
        lstCopy[i]*=-1
    return lstCopy
