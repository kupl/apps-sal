def crossing_sum(matrix, row, col):
    return sum(matrix[row]) + sum([matrix[a][col] for a in range(len(matrix)) if a != row])
