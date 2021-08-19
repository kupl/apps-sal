def has_exit(maze):
    def rec(i, j):
        if not i in range(len(maze)):
            return True
        if not j in range(len(maze[i])):
            return True
        if maze[i][j] == '#':
            return False
        maze[i][j] = '#'
        return any(rec(i + k, j + l) for k in (-1, 0, 1) for l in (-1, 0, 1) if bool(k) != bool(l))

    pos = None
    for i, line in enumerate(maze):
        for j, c in enumerate(line):
            if c == 'k':
                if pos:
                    raise Exception("There should not be multiple Kates")
                else:
                    pos = (i, j)
    if not pos:
        raise Exception("There should be a Kate")
    maze = list(map(list, maze))
    return rec(*pos)
