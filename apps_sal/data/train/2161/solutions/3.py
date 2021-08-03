def R(): return map(int, input().split())


n, m, w = R()
ws = [0] + list(R())
bs = [0] + list(R())
g = [[] for x in range(n + 1)]
for i in range(m):
    x, y = R()
    g[x].append(y)
    g[y].append(x)
cs = [0] * (n + 1)
cnt = 1
for i in range(1, n + 1):
    if not cs[i]:
        cs[i] = cnt
        q = []
        q.append(i)
        while q:
            nxt = q.pop()
            for x in g[nxt]:
                if not cs[x]:
                    cs[x] = cnt
                    q.append(x)
        cnt += 1
gs = [[] for i in range(cnt)]
for i in range(1, n + 1):
    gs[cs[i]].append(i)
dp = [[0] * (w + 1) for i in range(cnt)]
for i in range(1, cnt):
    tw = sum(ws[k] for k in gs[i])
    tb = sum(bs[k] for k in gs[i])
    for j in range(1, w + 1):
        dp[i][j] = max(dp[i][j], dp[i - 1][j], (dp[i - 1][j - tw] + tb if j >= tw else 0))
        for k in gs[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j], (dp[i - 1][j - ws[k]] + bs[k] if j >= ws[k] else 0))
print(dp[-1][w])
