def over_the_road(address, n):
    if address % 2 == 0:
        p = (n * 2 - address) / 2
        return 1 + 2 * p
    else:
        p = (n * 2 - 1 - address) / 2
        return 2 + 2 * p
