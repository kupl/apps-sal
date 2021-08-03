def path_finder(maze):
    maze = maze.split('\n')
    x_, y_ = len(maze) - 1, len(maze[0]) - 1
    DMap = {(0, 0): 1}
    exit, chkr = (x_, y_), len(DMap)
    while 1:
        for x, r in enumerate(maze):
            for y, c in enumerate(r):
                if maze[x][y] == '.' and not DMap.get((x, y)) and any(DMap.get(e) for e in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))):
                    DMap[(x, y)] = 1
        if chkr == len(DMap):
            break
        chkr = len(DMap)
    return DMap.get(exit, 0)
