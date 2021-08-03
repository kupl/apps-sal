def beggars(a, n):
    return [sum(a[i::n]) for i in range(n)]
