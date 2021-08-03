def multiplication_table(row, col):
    return [[i * j for i in range(1, col + 1)] for j in range(1, row + 1)]
