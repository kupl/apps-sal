def regressionLine(x, y):
    Ex2 = sum((i ** 2 for i in x))
    Exy = sum((i * j for (i, j) in zip(x, y)))
    Ex = sum(x)
    Ey = sum(y)
    n = len(x)
    return (round((Ex2 * Ey - Ex * Exy) / (n * Ex2 - Ex ** 2), 4), round((n * Exy - Ex * Ey) / (n * Ex2 - Ex ** 2), 4))
