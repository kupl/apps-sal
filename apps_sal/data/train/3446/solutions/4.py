def approx_root(n):
    base = int(n ** 0.5)
    diff_gn = n - base ** 2
    diff_lg = base * 2 + 1
    return round(base + diff_gn / diff_lg, 2)
