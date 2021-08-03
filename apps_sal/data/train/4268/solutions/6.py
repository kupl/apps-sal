from bisect import bisect


def rec(L, i): return L and (L + rec([y for x in L for y in range(10 * x, 10 * (x + 1)) if not y % i], i + 1))


polys = rec(list(range(1, 10)), 2)


def next_num(n):
    try:
        return polys[bisect(polys, n)]
    except IndexError:
        return
