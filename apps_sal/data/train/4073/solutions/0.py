def crossing_sum(matrix, row, col):
    return sum(matrix[row]) + sum((line[col] for line in matrix)) - matrix[row][col]
