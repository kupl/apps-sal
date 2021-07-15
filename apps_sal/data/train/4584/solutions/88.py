def invert(lst):
    list = []
    for i in range(0,len(lst)):
        a = -lst[i]
        list.append(a)
        i = i + 1
    return list
