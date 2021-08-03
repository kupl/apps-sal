MOVES = {(0, 1), (0, -1), (1, 0), (-1, 0)}


def has_exit(maze):
    posSet = {(x, y) for x in range(len(maze)) for y in range(len(maze[x])) if maze[x][y] == 'k'}
    if len(posSet) != 1:
        raise ValueError("There shouldn't be more than one kate")

    seen = set(posSet)
    while posSet:
        x, y = posSet.pop()
        if any(not (0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[x + dx])) for dx, dy in MOVES):
            return True
        neighbors = {(x + dx, y + dy) for dx, dy in MOVES if 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[x + dx])
                     and maze[x + dx][y + dy] == ' '
                     and (x + dx, y + dy) not in seen}
        posSet |= neighbors
        seen |= neighbors
    return False
