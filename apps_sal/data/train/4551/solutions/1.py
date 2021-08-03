def score_matrix(matrix):
    return sum(
        (-1)**(i + j) * x
        for i, row in enumerate(matrix)
        for j, x in enumerate(row)
    )
