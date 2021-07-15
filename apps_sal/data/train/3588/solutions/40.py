def quadratic(x1, x2):
    coff = [1]
    coff.append(-x2 - x1)
    coff.append(-x1 * -x2)
    return tuple(coff)
