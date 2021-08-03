def rotate_clockwise(matrix):
    matrix = [[c for c in line] for line in matrix]
    return [''.join(line) for line in zip(*matrix[::-1])]
