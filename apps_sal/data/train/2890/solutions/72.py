def multiples(m, n):
    list = []
    i = 1
    while i <= m:
        list = list + [i * n]
        i = i + 1
    return list
