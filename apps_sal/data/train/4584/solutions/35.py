def invert(lst):
    lst1 = []
    for x in range(len(lst)):
        if lst[x] > 0:
            y = -lst[x]
            lst1.append(y)
        elif lst[x] < 0:
            y = -lst[x]
            lst1.append(y)
        elif lst[x] == 0:
            lst1.append(0)
    return lst1
