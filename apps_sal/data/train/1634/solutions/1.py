inc = {}
dec = {}


def total_inc(n, a):
    if n not in inc:
        inc[n] = {}
    if a not in inc[n]:
        inc[n][a] = total_inc(n, a + 1) + total_inc(n - 1, a) if a < 9 and n > 0 else 1
    return inc[n][a]


def total_dec(n, a):
    if n not in dec:
        dec[n] = {}
    if a not in dec[n]:
        dec[n][a] = total_dec(n, a - 1) + total_dec(n - 1, a)if a > 0 and n > 0 else 1
    return dec[n][a]


def total_inc_dec(n):
    return total_inc(n, 0) + sum([total_dec(m, 9) for m in range(n + 1)]) - (10 * n + 1)
