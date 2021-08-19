def robot_transfer(matrix, k):
    r = 0
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            (x, y) = (i, j)
            for step in range(k):
                (x, y) = map(int, matrix[x][y].split(','))
                if x == i and y == j:
                    break
            if x == i and y == j and (step == k - 1):
                r += 1
    return r
