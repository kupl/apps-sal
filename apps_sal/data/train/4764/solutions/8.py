def rotate_clockwise(matrix):
    return [''.join(row) for row in zip(*reversed(matrix))]
