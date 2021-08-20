def over_the_road(address, n):
    if address % 2 == 1:
        x = n * 2 - (address + 1) + 2
    if address % 2 == 0:
        x = n * 2 - 1 - (address - 2)
    return x
