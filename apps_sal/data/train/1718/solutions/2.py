def has_exit(m):
    maze = [[x for x in row] for row in m]
    if not check_edge(maze):
        return False
    if not check_kate(maze):
        raise Exception('There should no be multiple Kates')
    kate = find_kate(maze)
    return find_way(maze, kate, kate)


def find_way(maze, position, previous_position, trace=[]):
    if is_exit(maze, position):
        return True
    possible_ways = find_possible_ways(maze, position, previous_position)
    for possible_way in possible_ways:
        if possible_way not in trace:
            new_maze = move_kate(maze, possible_way, position)
            if find_way(new_maze, possible_way, position, trace + [possible_way]):
                return True
    return False


def find_possible_ways(maze, position, previous_position):
    (r, c) = position
    possible_ways = []
    for (pr, pc) in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
        if pr >= 0 and pr < len(maze) and (pc >= 0) and (pc < len(maze[0])):
            if maze[pr][pc] == ' ' and (pr, pc) != previous_position:
                possible_ways += [(pr, pc)]
    return possible_ways


def find_kate(maze):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'k':
                return (r, c)


def move_kate(maze, new_position, previous_position):
    (nr, nc) = new_position
    (pr, pc) = previous_position
    new_m = maze[:pr] + [maze[pr][:pc] + [' '] + maze[pr][pc + 1:]] + maze[pr + 1:]
    return new_m[:nr] + [new_m[nr][:nc] + ['k'] + new_m[nr][nc + 1:]] + new_m[nr + 1:]


def check_edge(maze):
    edges = maze[0] + maze[-1] + tr(maze)[0] + tr(maze)[-1]
    if ' ' in edges or 'k' in edges:
        return True
    return False


def check_kate(maze):
    count = 0
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'k':
                count += 1
    return count == 1


def is_exit(maze, position):
    (width, length) = (len(maze) - 1, len(maze[0]) - 1)
    if width in position or length in position or 0 in position:
        return True
    return False


def tr(mtx):
    return [list(x) for x in zip(*mtx)]
