def crossing_sum(matrix, row, col):
    return sum(matrix[row]) + sum([matrix[a][col] for a in range(len(matrix)) if a != row])
    # sums the required row
    # sums a list made of the required column minus the value that is in the row
