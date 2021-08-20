def solve(n):
    t = 0
    for d in [500, 200, 100, 50, 20, 10]:
        (a, n) = divmod(n, d)
        t += a
    if n:
        return -1
    return t
