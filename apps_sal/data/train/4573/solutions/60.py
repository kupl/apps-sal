def over_the_road(address, n):
    if address % 2 == 1:
        return n * 2 - (address // 2) * 2
    else:
        return n * 2 - address + 1
