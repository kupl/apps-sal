def multiplication_table(row, col):
    return [[e * i for e in range(1, col + 1)] for i in range(1, row + 1)]
