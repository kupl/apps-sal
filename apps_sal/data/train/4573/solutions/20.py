def over_the_road(address, n):
    result = 0
    if address % 2 == 0:
        result = n * 2 - address + 1
    elif address % 2 == 1:
        result = n * 2 - (address - 1)
    return result
