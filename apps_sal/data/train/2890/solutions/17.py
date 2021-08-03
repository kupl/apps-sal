def multiples(m, n):
    list = []
    arr = 0
    for i in range(1, m + 1):
        arr = i * n
        list.append(arr)
    return list
