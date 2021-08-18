def g1(n): return (9 * (n + 1) * 10**n - 10**(n + 1) + 1) // 9


def g2(n): return int(''.join((str(n - 1), "8" * (n - 1), "9")))


L = [g1(x) for x in range(1, 1000)]


def champernowneDigit(n):
    if not (type(n) == int and 0 < n):
        return float("nan")
    if n == 1:
        return 0
    n -= 1
    x = next(i for i, v in enumerate(L, 1) if v > n)
    q, r = divmod(L[x - 1] - n, x)
    return int(str(10**x - 1 - q)[-r - 1])
