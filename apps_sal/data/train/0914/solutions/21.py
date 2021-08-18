t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    def get_ups(r, c): return [(r - 1, c + i) for i in [1, 0, -1] if 0 <= c + i < m]
    grid = [list(map(int, input().split())) for _ in range(n)]
    res = [[0] * m for _ in range(n)]
    res[0] = ['1'] * m
    for i in range(1, n):
        for j in range(m):
            t = 1
            for r, c in get_ups(i, j):
                if grid[r][c] > grid[i][j]:
                    grid[i][j] = grid[r][c]
                    t = 0
            res[i][j] = '1' if t else '0'
    for r in res:
        print(''.join(r))
