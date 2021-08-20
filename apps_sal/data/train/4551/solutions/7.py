def score_matrix(matrix):
    s = 0
    for (i, row) in enumerate(matrix):
        for (j, v) in enumerate(row):
            s += pow(-1, i + j) * v
    return s
