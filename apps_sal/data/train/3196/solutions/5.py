def tri(number):
    return int(number * (number + 1) / 2)


def quadsol(number):
    return int((math.sqrt(8 * number + 1) - 1) / 2)


def triangular_range(start, stop):
    return {x: tri(x) for x in range(quadsol(start), quadsol(stop) + 1) if tri(x) in range(start, stop + 1)}
