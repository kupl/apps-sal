def rotate_against_clockwise(matrix, times):
    if times == 0:
        return matrix
    else:
        matrix = [list(row) for row in zip(*matrix)][::-1]
        return rotate_against_clockwise(matrix, times % 4 - 1)
