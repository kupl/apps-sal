def rotate_clockwise(matrix):
    if not len(matrix): return []
    res = []
    for x in range(len(matrix[0])):
        temp = []
        for y in range(len(matrix)-1,-1,-1):
            temp.append(matrix[y][x])
        res.append(''.join(temp))
    return res
