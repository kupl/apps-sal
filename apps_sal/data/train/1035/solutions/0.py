from collections import namedtuple
CurrentPosition = namedtuple('current_position', 'points, cell, pairs')
T = int(input())
for _ in range(T):
    (R, C, N) = map(int, input().split())
    (Sx, Sy) = map(int, input().split())
    tx = map(int, input().split())
    ty = map(int, input().split())
    tel_pairs = list(zip(tx, ty))
    board = []
    for _ in range(R):
        board += [[int(c) for c in input().split()]]

    def explore(p):
        next_pos = []
        for (i, (dx, dy)) in enumerate(p.pairs):
            (sx, sy) = p.cell
            new_pairs = p.pairs[:i] + p.pairs[i + 1:]
            (px, py) = (sx + dx, sy + dy)
            if px < R and py < C:
                next_pos += [CurrentPosition(p.points + board[px][py], (px, py), new_pairs)]
            (px, py) = (sx + dx, sy - dy)
            if px < R and 0 <= py:
                next_pos += [CurrentPosition(p.points + board[px][py], (px, py), new_pairs)]
            (px, py) = (sx - dx, sy + dy)
            if 0 <= px and py < C:
                next_pos += [CurrentPosition(p.points + board[px][py], (px, py), new_pairs)]
            (px, py) = (sx - dx, sy - dy)
            if 0 <= px and 0 <= py:
                next_pos += [CurrentPosition(p.points + board[px][py], (px, py), new_pairs)]
        return next_pos
    pos = [CurrentPosition(board[Sx][Sy], (Sx, Sy), tel_pairs)]
    result = board[Sx][Sy]
    while pos:
        p = pos.pop(0)
        if p.pairs:
            pos += explore(p)
        else:
            result = max(result, p.points)
    print(result)
