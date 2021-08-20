def over_the_road(address, n):
    if address // 2 == 0:
        return 2 * ((address - 2 * n - 2) / -2) - 1
    else:
        return 2 * (n + 1 - (address + 1) / 2)
