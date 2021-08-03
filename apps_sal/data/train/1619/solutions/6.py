def dec(r, d):
    for i in range(d - 1, 0, -1):
        if r < i * i:
            continue
        if r == i * i:
            return [i]
        a = dec(r - i * i, i)
        if a:
            return a + [i]
    return None


def decompose(n):
    return dec(n * n, n)
