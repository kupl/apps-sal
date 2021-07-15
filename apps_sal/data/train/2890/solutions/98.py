def multiples(m, n):
    list = []
    for i in range(1,m):
        list.append(i * n)
    list.append(m*n)
    return list
