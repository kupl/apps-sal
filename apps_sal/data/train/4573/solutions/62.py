def over_the_road(address, n):
    if address % 2 == 0:
        return 2 * n - address + 1
    else:
        index = int((address + 1) / 2)
        return 2 * n - 2 * (index - 1)
