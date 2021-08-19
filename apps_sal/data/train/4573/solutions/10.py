def over_the_road(address, n):
    if address % 2 == 0:
        return int(n * 2 - 1 - (address / 2 - 1) * 2)
    else:
        return int(n * 2 - ((address + 1) / 2 - 1) * 2)
