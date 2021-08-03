def f(n, s=0):
    c, li = 10 + s, list(range(1 + s, 10 + s))
    for i in range(n - 1):
        c += sum(li)
        li = [sum(li[:k + 1]) + s for k in range(len(li))]
    return c - s


def total_inc_dec(n): return (f(n) + f(n, 1) - (10 + 9 * (n - 1))) if n else 1
