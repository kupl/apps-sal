def over_the_road(address, n):
    return 1 + (n * 2 - address) if address % 2 == 0 else n * 2 - (address - 1)
