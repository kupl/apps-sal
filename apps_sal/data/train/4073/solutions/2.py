def crossing_sum(matrix, row, col):
    return sum(matrix[row]) + sum(i[col] for i in matrix[:row] + matrix[row + 1:])
