from functools import reduce
def comb(n): return reduce(lambda x, y: x * y, range(n + 9, n + 1, -1)) // 40320
def f(n): return (n**2 + 21 * n + 20) * comb(n) // 90 - 10 * n - 2


def insane_inc_or_dec(x):
    return f(x) % 12345787
