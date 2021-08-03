def over_the_road(address, n):
    if address % 2 == 0:
        return 2 * (n - (address / 2 - 1) - 1) + 1
    else:
        return 2 * (n - (address - 1) / 2)
