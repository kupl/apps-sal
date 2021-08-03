from copy import deepcopy


def reverse_on_diagonals(matrix):
    matrix = deepcopy(matrix)
    n = len(matrix)
    for y in range(n // 2):
        x = n - y - 1
        matrix[y][y], matrix[x][x] = matrix[x][x], matrix[y][y]
        matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
    return matrix
