def approx_root(n):
    b = int(n ** 0.5)
    diff_gn = n - b**2
    diff_lg = (b + 1)**2 - b**2
    return round(b + (diff_gn / diff_lg), 2)
