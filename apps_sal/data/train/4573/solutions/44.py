def over_the_road(address, n):
    return 2 * (n - address // 2) if address % 2 else 2 * (n - address // 2) + 1
