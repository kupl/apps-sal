directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def how_many_bees(hive):
    r, c = (len(hive), len(hive[0])) if hive else (0, 0)
    def f(s, i, j, di, dj):
        if not (0 <= i < r and 0 <= j < c and s.startswith(hive[i][j])):
            return 0
        s = s[1:]
        return f(s, i+di, j+dj, di, dj) if s else 1
    return sum(f('bee', i, j, di, dj) for i in range(r) for j in range(c) for di, dj in directions)
