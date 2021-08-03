def R(): return map(int, input().split())


n, m, w = R()
ws = list(R())
bs = list(R())
anc = [-1] * n


def get(x):
    if anc[x] < 0:
        return x
    anc[x] = get(anc[x])
    return anc[x]


def join(x1, x2):
    x1, x2 = get(x1), get(x2)
    if x1 != x2:
        anc[x1] = x2


for i in range(m):
    x1, x2 = R()
    join(x1 - 1, x2 - 1)
gs = [list() for i in range(n)]
for i in range(n):
    gs[get(i)].append(i)
gs = [x for x in gs if x]
dp = [[0] * (w + 1) for i in range(len(gs) + 1)]
for i in range(len(gs)):
    tw = sum(ws[k] for k in gs[i])
    tb = sum(bs[k] for k in gs[i])
    for j in range(w + 1):
        dp[i][j] = max(dp[i][j], dp[i - 1][j], (dp[i - 1][j - tw] + tb if j >= tw else 0))
        for k in gs[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j], (dp[i - 1][j - ws[k]] + bs[k] if j >= ws[k] else 0))
print(dp[len(gs) - 1][w])
