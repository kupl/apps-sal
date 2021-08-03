def fibLikeGen():
    a, b = (1, 0), (0, 1)                  # a: station i-1, b: station i
    while 1:
        yield a, b
        a, b = b, tuple(x + y for x, y in zip(a, b))


gen = fibLikeGen()
SUM_AT = [(), (1, 0), (1, 0)]             # (k,l)


def getCoefs(n):
    while len(SUM_AT) <= n:
        a, b = next(gen)
        SUM_AT.append(tuple(x + y for x, y in zip(a, SUM_AT[-1])))
    return SUM_AT[n]


def calc(k, n, m, x):
    a, b = getCoefs(n - 1)
    l = (m - a * k) // b
    a, b = getCoefs(x)
    return a * k + b * l
