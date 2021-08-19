def approx_root(n):
    for i in range(1, int(n ** 0.5) + 2):
        if i ** 2 > n:
            base = i - 1
            break
    base2 = base + 1
    diff_gn = n - base ** 2
    diff_lg = base2 ** 2 - base ** 2
    return round(base + diff_gn / diff_lg, 2)
