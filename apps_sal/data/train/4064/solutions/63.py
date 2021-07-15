def count_by(x, n):
    count = 1
    i = 1
    L = []
    while count <= n:
        if i % x == 0:
            L.append(i)
            count += 1
        i += 1
    return L

