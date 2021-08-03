def multiples(m, n):
    lst = []
    for x in range(1, m + 1):
        y = n * x
        lst.append(y)
    return lst
