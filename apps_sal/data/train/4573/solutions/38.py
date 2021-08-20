def over_the_road(address, n):
    x = 0
    if address in range(2 * n, 0, -2):
        x = range(2 * n, 0, -2).index(address)
        return range(1, 1 + 2 * n, 2)[x]
    elif address in range(1, 1 + 2 * n, 2):
        x = range(1, 1 + 2 * n, 2).index(address)
        return range(2 * n, 0, -2)[x]
