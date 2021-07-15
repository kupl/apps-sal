def rotate_clockwise(matrix):
    return [''.join(l)[::-1] for l in zip(*matrix)]
