def over_the_road(address, n):
    if address % 2 != 0:
        position = (address + 1) / 2
        neighbor = (n - position + 1) * 2
    else:
        position = - (address / 2) + n + 1
        neighbor = (position * 2) - 1
    return neighbor
