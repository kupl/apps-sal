import decimal


def sum_cubes(n):
    n = decimal.Decimal(n)
    return n**2 * (n + 1)**2 / 4
