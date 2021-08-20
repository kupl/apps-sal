def findSquares(m, n):
    return sum(((m - i) * (n - i) for i in range(min(m, n))))
