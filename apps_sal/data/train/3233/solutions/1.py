def robot_transfer(matrix, k):
    (res, seen) = (0, set())
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i, j) in seen:
                continue
            (x, y, S) = (i, j, {(i, j)})
            for _ in range(k):
                (x, y) = map(int, matrix[x][y].split(','))
                S.add((x, y))
            if (x, y) == (i, j) and len(S) == k:
                res += k
                seen |= S
    return res
