def cheapest_quote(n):

    if n < 1:
        return 0

    bundles = iter([(40, 3.85), (20, 1.93), (10, 0.97), (5, 0.49), (1, 0.1)])
    total = 0

    while n > 0:
        size, price = next(bundles)
        if size <= n:
            q, n = divmod(n, size)
            total += q * price

    return round(total, 2)
