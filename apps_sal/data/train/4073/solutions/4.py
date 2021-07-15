def crossing_sum(matrix, row, col):
    return sum(matrix[row]) + sum(matrix[i][col] for i in range(len(matrix))) - matrix[row][col]

