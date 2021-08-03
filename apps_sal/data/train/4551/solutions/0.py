def score_matrix(matrix):
    return sum((-1) ** (i + j) * matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])))
