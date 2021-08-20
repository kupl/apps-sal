def robot_transfer(matrix, k):
    count = 0
    for (start_y, row) in enumerate(matrix):
        for (start_x, point) in enumerate(row):
            (y, x) = (int(point[0]), int(point[2]))
            for t in range(k - 1):
                (y, x) = (int(matrix[y][x][0]), int(matrix[y][x][2]))
                if (y, x) == (start_y, start_x):
                    count += t + 2 == k
                    break
    return count
