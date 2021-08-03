def f(matrix, k, i, j):
    i0, j0 = i, j
    for n in range(1, k + 1):
        i, j = matrix[i][j]
        if i == i0 and j == j0:
            return n == k
    return False


def robot_transfer(matrix, k):
    matrix = [
        [tuple(map(int, x.split(','))) for x in row]
        for row in matrix
    ]
    return sum(
        f(matrix, k, i, j)
        for i, row in enumerate(matrix)
        for j, x in enumerate(row)
    )
