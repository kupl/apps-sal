def rotate_clockwise(matrix):
    return ["".join(i) for i in zip(*reversed(matrix))] 
