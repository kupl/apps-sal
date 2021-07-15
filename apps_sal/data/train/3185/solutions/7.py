def rotate_against_clockwise(matrix, times):
    for i in range(3 - (times + 3) % 4):
        matrix = list(map(list, zip(*matrix[::-1])))
    return matrix
