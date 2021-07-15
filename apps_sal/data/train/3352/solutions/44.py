def find_longest(arr):
    lst = []
    empty = []
    for i in arr:
        i = str(i)
        lst.append(len(i))
    for j in lst:
        empty.append(j)
    empty.sort()
    maxvaldig = empty[-1]
    if empty.count(maxvaldig) > 1:
        index = lst.index(maxvaldig)
        realmaxval = arr[index]
    else:
        index = lst.index(maxvaldig)
        realmaxval = arr[index]
        
    return realmaxval
