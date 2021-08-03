def different_squares(mat):
    v = set()
    for i in range(len(mat) - 1):
        for j in range(len(mat[0]) - 1):
            v.add((mat[i][j], mat[i][j + 1], mat[i + 1][j], mat[i + 1][j + 1]))

    return len(v)
