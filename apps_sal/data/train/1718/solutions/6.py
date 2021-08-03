def has_exit(maze):
    start = [[i, maze[i].find('k')] for i in range(len(maze)) if maze[i].find('k') != -1]
    if len(start) != 1:
        raise Exception("There should no be multiple Kates")
    if backtracking(maze, start[0][0], start[0][1], set()):
        return True
    return False


def backtracking(maze, y, x, explored):
    if maze[y][x] == '#':
        explored.add((y, x))
        return False
    if (y, x) in explored:
        return False
    if x in {0, len(maze[0]) - 1} or y in {0, len(maze) - 1}:
        return True
    explored.add((y, x))
    found = backtracking(maze, y - 1, x, explored) or\
        backtracking(maze, y, x + 1, explored) or\
        backtracking(maze, y + 1, x, explored) or\
        backtracking(maze, y, x - 1, explored)
    return found
