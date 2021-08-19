def path_finder(maze):
    maze = [list(level) for level in maze.split('\n')]
    N = len(maze)
    Q = [(0, 0)]
    while Q:
        (x, y) = Q.pop(0)
        if x >= 0 and y >= 0 and (x < N) and (y < N):
            if x == N - 1 and y == N - 1:
                return True
            if maze[y][x] == '.':
                maze[y][x] = 'W'
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for (dx, dy) in directions:
                    Q.append((x + dx, y + dy))
    return False
