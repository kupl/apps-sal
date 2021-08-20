def path_finder(maze):
    maze = maze.split('\n')
    mazeD = {(x, y): 1 for (x, e) in enumerate(maze) for (y, _) in enumerate(e) if _ == '.'}
    (exit, DMap, stack) = ((len(maze) - 1, len(maze[0]) - 1), {}, [(0, 0)])
    while stack:
        (x, y) = stack.pop()
        if not DMap.get((x, y)):
            DMap[x, y] = 1
            for (xc, yc) in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
                if mazeD.get((xc, yc)):
                    stack.append((xc, yc))
    return DMap.get(exit, 0)
