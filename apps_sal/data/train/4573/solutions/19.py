def over_the_road(address, n):
    if address % 2 == 1:
        return 2*(n - address//2)
    return 1 + 2*(n - address//2)
