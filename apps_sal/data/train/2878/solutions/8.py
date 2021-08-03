def shortest_to_char(s, c):
    if not s or not c:
        return []
    a = [i for i, x in enumerate(s) if x == c]
    if not a:
        return []
    r, n = [0] * len(s), 0
    for x, y in zip(a, a[1:] + [None]):
        m = (x + y + 1) // 2 if y is not None else len(s)
        while n < m:
            r[n] = abs(n - x)
            n += 1
    return r
