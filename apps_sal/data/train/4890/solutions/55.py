def find_difference(a, b):
    volA = 1
    volB = 1
    for x, y in zip(a, b):
        volA = volA * x
        volB = volB * y

    return abs(volA - volB)
