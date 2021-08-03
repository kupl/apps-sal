def simplify(path):
    moves = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
    rev_moves = {(0, 0): '', (0, 1): '^', (0, -1): 'v', (-1, 0): '<', (1, 0): '>'}
    x, y = 0, 0
    visited = [(0, 0)]
    for p in path:
        mov = moves[p]
        x1, y1 = x + mov[0], y + mov[1]
        if not (x1, y1) in visited:
            visited.append((x1, y1))
        else:
            idx = visited.index((x1, y1))
            visited = visited[0:idx + 1]
        x, y = x1, y1
    last = (0, 0)
    res = ''
    for p in visited:
        dx, dy = p[0] - last[0], p[1] - last[1]
        res += rev_moves[(dx, dy)]
        last = p
    return res
