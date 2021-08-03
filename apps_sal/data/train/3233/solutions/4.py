def robot_transfer(matrix, k):
    cycles = 0
    for x, l in enumerate(matrix):
        for y, _ in enumerate(l):
            u, v = x, y
            for n in range(k):
                u, v = map(int, matrix[u][v].split(','))
                if (x, y) == (u, v):
                    cycles += n == k - 1
                    break
    return cycles
