def different_squares(matrix):
    (m, n) = (len(matrix), len(matrix[0]))
    return len({tuple(matrix[i][j:j + 2] + matrix[i + 1][j:j + 2]) for i in range(m - 1) for j in range(n - 1)})
