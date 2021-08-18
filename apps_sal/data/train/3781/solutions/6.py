def p(n, z=2):
    r = []
    s = 0
    for i in range(z, int(n**.5) + 1):
        if n % i == 0:
            x, y = p(n // i, i)
            s += x + 1
            r += [[i] + v for v in y] + [[i, n // i]]
    return s, r


def prod_int_partII(n, l):
    s, r = p(n)
    x = [v for v in r if len(v) == l]
    L = len(x)
    if L == 1:
        x = x[0]
    return[s, L, x]
