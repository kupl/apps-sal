def findSquares(x, y):
    if x > y:
        (x, y) = (y, x)
    return x * (x + 1) * (2 * x + 1) / 6 + (y - x) * x * (x + 1) / 2
