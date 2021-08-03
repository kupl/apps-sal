def path_finder(maze):

    maze = maze.split('\n')
    inf = 2147483647  # infinity
    n = len(maze)  # maze order
    distance_table = [[-1] * (n + 2) for i in range(n + 2)]  # distance table with boundaries

    for i in range(n + 2):  # mark boundary
        distance_table[0][i] = inf
        distance_table[n + 1][i] = inf
        distance_table[i][0] = inf
        distance_table[i][n + 1] = inf

    distance_table[1][1] = 0  # start position

    queue = [(1, 1)]  # start with (1,1)
    while queue:  # while queue is not empty
        i, j = queue.pop(0)
        for x, y in (0, 1), (0, -1), (-1, 0), (1, 0):  # east-(0,1); west-(0,-1); north-(-1,0); south-(1,0)
            p, q = i + x, j + y
            if distance_table[p][q] < inf:  # if its not boundary or a wall
                if maze[p - 1][q - 1] == 'W':  # if its a wall
                    distance_table[p][q] = inf
                elif distance_table[p][q] == -1 or distance_table[p][q] > distance_table[i][j] + 1:  # if the path is not visited or the path have longer distance
                    distance_table[p][q] = distance_table[i][j] + 1
                    queue.append((p, q))
    return False if distance_table[n][n] == -1 else distance_table[n][n]
