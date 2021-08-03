def over_the_road(address, n):
    return 2 * (n - address // 2) + ((address + 1) % 2) * 1
