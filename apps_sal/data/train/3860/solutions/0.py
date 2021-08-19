def how_many_apples(n):
    return n ** n - (n - 1) + [0, 4][n == 2]
