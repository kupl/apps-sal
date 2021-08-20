def path_finder(maze):
    maze = maze.split('\n')
    n = len(maze)
    reachable = [[None] * (n + 2) for i in range(n + 2)]
    for i in range(n + 2):
        reachable[0][i] = False
        reachable[n + 1][i] = False
        reachable[i][0] = False
        reachable[i][n + 1] = False
    queue = [(1, 1)]
    while queue:
        (i, j) = queue.pop(0)
        reachable[i][j] = True
        for (x, y) in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            (p, q) = (i + x, j + y)
            if reachable[p][q] == None:
                if maze[p - 1][q - 1] == '.':
                    reachable[p][q] = True
                    queue.append((p, q))
                else:
                    reachable[p][q] = False
    return False if reachable[n][n] == None else reachable[n][n]
