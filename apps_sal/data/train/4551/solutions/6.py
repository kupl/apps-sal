def score_matrix(matrix):
    return sum(n * (-1)**(i + j) for j, row in enumerate(matrix) for i, n in enumerate(row))
