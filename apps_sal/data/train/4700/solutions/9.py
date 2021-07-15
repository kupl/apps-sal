def solve(a):
    r_min = r_max = 1
    for x in a:
        cur = [n * m for n in [min(x), max(x)] for m in [r_min, r_max]]
        r_min = min(cur)
        r_max = max(cur)
    return r_max
