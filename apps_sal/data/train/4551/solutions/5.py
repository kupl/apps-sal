def score_matrix(matrix):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i + j) % 2 == 0:
                res += matrix[i][j]
            else:
                res -= matrix[i][j]
    return res
