def solve(n):
    if n % 10:
        return -1
    (c, billet) = (0, iter((500, 200, 100, 50, 20, 10)))
    while n:
        (x, r) = divmod(n, next(billet))
        (c, n) = (c + x, r)
    return c
