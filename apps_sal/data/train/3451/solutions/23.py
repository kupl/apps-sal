def triangle(row):
    COMB_I = [[0, 2, 1], [2, 1, 0], [1, 0, 2]]
    IDX = {'R': 0, 'G': 1, 'B': 2}
    IDX_R = {0: 'R', 1: 'G', 2: 'B'}
    ri = [IDX[r] for r in row]
    for k in range(len(row) - 1):
        ri = [COMB_I[i][j] for (i, j) in zip(ri[:-1], ri[1:])]
    return IDX_R[ri[0]]
