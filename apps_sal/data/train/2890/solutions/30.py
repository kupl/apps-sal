def multiples(m, n):
    list = []
    count = 1
    while count <= m:
        list.append(n * count)
        count += 1
    return list
