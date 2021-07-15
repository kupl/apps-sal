def robot_transfer(matrix, k):
    result = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            x, y, back = i, j, 0
            for _ in range(k):
                x, y = (int(n) for n in matrix[x][y].split(","))
                back += ((i, j) == (x, y))
            result += ((i, j) == (x, y) and back == 1)
    return result


