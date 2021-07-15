def approx_root(n):
    import math
    s = int(math.sqrt(n))
    diff_gn = n - s ** 2
    diff_lg = (s + 1) ** 2 - s ** 2
    return round(s + diff_gn / diff_lg, 2)
