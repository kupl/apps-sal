def reduce_fraction(fraction):
    n1, n2 = fraction[0], fraction[1]
    for i in range(2, 999):
        if n1 % i == 0 and n2 % i == 0:
            n1, n2 = n1 // i, n2 // i
            fraction = reduce_fraction([n1, n2])
    return tuple(fraction)
