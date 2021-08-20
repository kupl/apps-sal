def atomic_number(n):
    L = []
    i = 1
    while n > 0:
        a = min(2 * i ** 2, n)
        L.append(a)
        n -= a
        i += 1
    return L
