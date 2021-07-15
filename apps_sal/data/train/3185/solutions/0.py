def ccw(matrix):
    return [list(row) for row in zip(*map(reversed, matrix))]

def rotate_against_clockwise(matrix, times):
    for __ in range(times % 4):
        matrix = ccw(matrix)
    return matrix
