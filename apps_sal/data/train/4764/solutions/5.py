def rotate_clockwise(matrix):
    return list(map(''.join, zip(*matrix[::-1])))
