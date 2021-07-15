def rotate_clockwise(matrix):
    return list("".join(row) for row in zip(*matrix[::-1]))
