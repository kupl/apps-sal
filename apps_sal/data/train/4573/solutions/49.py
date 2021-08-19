def over_the_road(address, n):
    if address % 2 == 0:
        return 1 + 2 * (n - address / 2)
    else:
        return 2 * (n - address // 2)
