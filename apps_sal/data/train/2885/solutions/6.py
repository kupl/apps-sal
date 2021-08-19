def champernowneDigit(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        return float('nan')
    n -= 1
    sc = [9 * (x + 1) * pow(10, x) for x in range(50)]
    i = 0
    while n > sc[i]:
        n -= sc[i]
        i += 1
    (L, d) = divmod(n - 1, i + 1)
    return int(str(pow(10, i) + L)[d])
