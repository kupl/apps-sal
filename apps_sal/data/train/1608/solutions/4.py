def determinant(matrix):
    return reduce(lambda r, i: r + (-1)**i * matrix[0][i] * determinant([m[:i] + m[i + 1:] for m in matrix[1:]]), range(len(matrix[0])), 0) if len(matrix) != 1 else matrix[0][0]
