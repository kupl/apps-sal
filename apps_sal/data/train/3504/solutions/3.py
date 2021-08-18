def rests(n, b):
    rests = []
    while n:
        n, r = divmod(n, b)
        rests.append(r)
    return rests


def power_mod(x, y, n, k=5):
    base, table, res = 2 << (k - 1), [1], 1
    for i in range(1, base):
        table.append(x * table[i - 1] % n)
    for rest in reversed(rests(y, base)):
        for _ in range(k):
            res = res * res % n
        if rest:
            res = res * table[rest] % n
    return res
