def over_the_road(address, n):
    return 1 + (2 * n - address) if address % 2 == 0 else (2 * n) - (address - 1)
