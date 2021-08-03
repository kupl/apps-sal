from math import floor


def over_the_road(address, n):
    return (n - floor((address - 1) / 2)) * 2 - ((address + 1) % 2)
