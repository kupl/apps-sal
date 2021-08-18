def find(n):
    a = list(range(5, (n) + 1, 5))
    b = list(range(3, (n) + 1, 3))

    c = set(a)
    d = set(b)

    e = list(d - c)

    return sum(a + e)
