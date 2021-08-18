maxn = 50 + 10
g = [None] * maxn
dp = [None] * maxn
c = [None] * maxn
size = [0] * maxn

for i in range(0, maxn):
    c[i] = [0] * maxn
    c[i][0] = 1
    for j in range(1, i + 1):
        c[i][j] = c[i - 1][j - 1] + c[i - 1][j]

n = int(input())
for i in range(1, n + 1):
    g[i] = []
for i in range(1, n):
    u, v = input().split()
    u = int(u)
    v = int(v)
    g[u].append(v)
    g[v].append(u)


def mul(a, b, x, y):
    tmp = [0] * (x + y + 1)
    for i in range(0, x + 1):
        for j in range(0, y + 1):
            tmp[i + j] += a[i] * b[j] * c[i + j][i] * c[x + y - i - j][x - i]
    return tmp


def dfs(pos, fa):
    nonlocal dp
    nonlocal size
    dp[pos] = [1]
    size[pos] = 0
    for ch in g[pos]:
        if ch != fa:
            dfs(pos=ch, fa=pos)
            dp[pos] = mul(dp[pos], dp[ch], size[pos], size[ch])
            size[pos] += size[ch]
    if fa:
        size[pos] += 1
        tmp = [0] * (size[pos] + 1)
        for i in range(0, size[pos] + 1):
            for j in range(0, size[pos]):
                if j < i:
                    tmp[i] += dp[pos][i - 1]
                else:
                    tmp[i] += dp[pos][j] * 0.5
        dp[pos] = tmp


for i in range(1, n + 1):
    dfs(pos=i, fa=0)
    tmp = dp[i][0]
    for j in range(1, n):
        tmp /= j
    print(tmp)
