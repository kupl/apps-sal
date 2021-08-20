def over_the_road(address, n):
    address = int(address)
    if address % 2 == 0:
        return n * 2 - (address - 1)
    else:
        return n * 2 - address + 1
