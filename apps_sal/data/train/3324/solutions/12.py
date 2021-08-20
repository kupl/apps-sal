def sale_hotdogs(n):
    return n * [90, [95, 100][n < 5]][n < 10]
