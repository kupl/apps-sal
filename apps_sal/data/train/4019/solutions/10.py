def max_multiple(d, b):
    L = []
    for i in range(0, b + 1):
        if i % d == 0:
            L.append(i)
    return max(L)
