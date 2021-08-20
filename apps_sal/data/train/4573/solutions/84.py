def over_the_road(address, n):
    if address % 2 == 0:
        x = n - address / 2
        return int(1 + 2 * x)
    else:
        x = n - (address + 1) / 2
        return int(2 + 2 * x)
