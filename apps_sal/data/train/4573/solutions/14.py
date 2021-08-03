def over_the_road(address, n):
    if (address % 2) == 0:
        i = (2 * n - address) / 2
        return int(2 * i + 1)
    else:
        i = (address - 1) / 2
        return int(2 * n - 2 * i)
