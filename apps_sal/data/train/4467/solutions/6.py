def remember(str):
    lst = []
    for (i, j) in enumerate(str):
        if j in str[:i] and j not in lst:
            lst.append(j)
    return lst
