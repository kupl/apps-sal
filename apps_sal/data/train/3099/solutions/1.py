from string import ascii_letters as rows
ROWS = {c: n for n, c in enumerate(rows[26:] + rows[:26])}
DIRS = [(1, 0), (1, 1), (0, 1), (-1, 1)]


def whoIsWinner(moves, connect, size):
    def check_line(dx, dy):
        n = 0
        for _ in range(2):
            dx, dy, x, y = -dx, -dy, p, q
            while (0 <= x < size and 0 <= y < len(grid[x])
                   and grid[x][y] == player):
                n += 1
                x += dx
                y += dy
        return n > connect

    grid = [[] for _ in range(size)]
    for move in moves:
        row, player = move.split('_')
        p = ROWS[row]
        q = len(grid[p])
        grid[p].append(player)
        if any(check_line(u, v) for u, v in DIRS):
            return player
    return 'Draw'
