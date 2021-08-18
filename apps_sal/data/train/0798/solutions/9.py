def ipnl(n): return [int(input()) for _ in range(n)]


def inp(): return int(input())
def ip(): return [int(w) for w in input().split()]


n, m = ip()
grid = []
for i in range(n):
    grid.append(ip())
mat = [[0 for i in range(n + 1)] for j in range(n + 1)]
for _ in range(m):
    a, b, k = ip()
    f = 0
    for j in range(b - k, b + k + 1):
        if 0 < j <= n:
            for i in range(a - f, a + f + 1):
                if 0 < i <= n:
                    mat[i][j] = 1
        if j < b:
            f += 1
        else:
            f -= 1
for i in range(n + 1):
    mat[i][0] = -1
    mat[0][i] = -1
grid.insert(0, [float('-inf') for i in range(n)])
for i in range(len(grid)):
    grid[i].insert(0, float('-inf'))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if mat[i - 1][j] == 0 and mat[i][j - 1] == 0:
            mat[i][j] = 0
        else:
            a, b = float('-inf'), float('-inf')
            if mat[i - 1][j] != 0:
                a = grid[i - 1][j]
            if mat[i][j - 1] != 0:
                b = grid[i][j - 1]
            if not (i == 1 and j == 1):
                grid[i][j] += max(a, b)
if mat[-1][-1] == 0 or mat[1][1] == 0:
    print("NO")
else:
    print("YES")
    print(grid[-1][-1])
