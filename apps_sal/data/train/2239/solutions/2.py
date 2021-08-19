import sys
# sys.setrecursionlimit(10**5)
n, m = map(int, input().split())
g = {i: [] for i in range(1, n + 1)}
dp = [[[-1] * 26 for _ in range(n + 1)] for i in range(n + 1)]


def rec(i, j, ch):
    if dp[i][j][ord(ch) - ord('a')] != -1:
        return dp[i][j][ord(ch) - ord('a')]
    for x in g[i]:
        if ord(x[1]) >= ord(ch):
            v = rec(j, x[0], x[1])
            if not v:
                dp[i][j][ord(ch) - ord('a')] = 1
                return 1
    dp[i][j][ord(ch) - ord('a')] = 0
    return 0


for _ in range(m):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = line[2]
    g[a].append([b, c])
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print('A', end="") if rec(i, j, 'a') else print('B', end="")
    print()
