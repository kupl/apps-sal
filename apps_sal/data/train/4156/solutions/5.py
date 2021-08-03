def findSquares(x, y):
    S = 0
    for i in range(y):
        S += (x - i) * (y - i)

    return S
