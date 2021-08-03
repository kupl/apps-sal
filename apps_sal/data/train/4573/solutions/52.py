def over_the_road(address, n):
    if address % 2 == 0:
        address = n * 2 - address
        return 1 + address
    else:
        address = address - 1
        return n * 2 - address
