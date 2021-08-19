def crossing_sum(matrix, row, col):
    a = matrix[row]
    b = [i[col] for (num, i) in enumerate(matrix) if num != row]
    return sum(a) + sum(b)
