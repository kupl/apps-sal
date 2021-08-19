MOD = 20011


def lego(x, y, consec, prev):
    if x >= r or y >= c:
        return 0
    if grid[x][y] == 0:
        return 0
    if x == r - 1 and y == c - 1:
        return 1
    if dp[x][y][consec][prev] != -1:
        return dp[x][y][consec][prev]
    if consec == 0:
        if prev == 0:
            dp[x][y][consec][prev] = lego(x, y + 1, d - 1, 1) % MOD
        else:
            dp[x][y][consec][prev] = lego(x + 1, y, d - 1, 0) % MOD
    elif prev == 0:
        dp[x][y][consec][prev] = (lego(x + 1, y, consec - 1, 0) + lego(x, y + 1, d - 1, 1)) % MOD
    else:
        dp[x][y][consec][prev] = (lego(x, y + 1, consec - 1, 1) + lego(x + 1, y, d - 1, 0)) % MOD
    return dp[x][y][consec][prev]


(r, c, d) = map(int, input().split())
grid = []
for i in range(r):
    alpha = list(map(int, input().split()))
    grid.append(alpha)
dp = [[[[-1, -1] for z in range(d)] for j in range(c)] for i in range(r)]
print((lego(1, 0, d - 1, 0) + lego(0, 1, d - 1, 1)) % MOD)
