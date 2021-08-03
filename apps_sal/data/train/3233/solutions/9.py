def robot_transfer(matrix, k):
    N = len(matrix)
    mat = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            mat[i][j] = (int(matrix[i][j][0]), int(matrix[i][j][2]))
    tot = 0
    for i in range(N):
        for j in range(N):
            y = (i, j)
            for kk in range(k):
                y = mat[y[0]][y[1]]
                if y == (i, j) and kk < k - 1:
                    break
            if y == (i, j) and kk == k - 1:
                tot += 1
    return tot
