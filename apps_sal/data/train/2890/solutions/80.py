def multiples(m, n):
    lis = []
    for x in range(1, m + 1, 1):
        lis.append(n * x)
    return lis
