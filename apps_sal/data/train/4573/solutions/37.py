def over_the_road(address, n):
    house = (address + 1) / 2
    opposite = int(n * 2 - ((house - 1) * 2))
    return opposite
