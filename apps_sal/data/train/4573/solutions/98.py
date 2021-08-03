def over_the_road(address, n):
    return (2 * n - address) + 1 if address % 2 == 0 else ((2 * n - 1) - address) + 2
