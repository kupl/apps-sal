def four_piles(n, y):
    (x, r) = divmod(n * y, (y + 1) ** 2)
    return [] if r or x == y else [x + y, x - y, x * y, x // y]
