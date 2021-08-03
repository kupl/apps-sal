def path_finder(maze):
    maze = list(map(list, maze.splitlines()))
    lenmaze_y, lenmaze_x = len(maze), len(maze[0])
    queue = [(0, 0, 0)]

    while queue:
        y, x, cnt = queue.pop(0)
        if x >= 0 and y >= 0 and x < lenmaze_x and y < lenmaze_y:
            if maze[y][x] == '.':
                maze[y][x] = cnt
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for direction_y, direction_x in directions:
                    queue.append((y + direction_y, x + direction_x, cnt + 1))
            if x == lenmaze_x - 1 and y == lenmaze_y - 1:
                return maze[y][x]

    return False
