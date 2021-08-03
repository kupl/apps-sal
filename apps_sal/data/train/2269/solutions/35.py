import sys
input = sys.stdin.readline


def is_bipartite(graph, s):
    """二部グラフ判定する"""
    n = len(graph)
    col = [-1] * n
    col[s] = 0
    stack = [s]
    used[s] = True
    while stack:
        v = stack.pop()
        for nxt_v in graph[v]:
            used[nxt_v] = True
            if col[nxt_v] == -1:
                col[nxt_v] = col[v] ^ 1
                stack.append(nxt_v)
            elif col[nxt_v] ^ col[v] == 0:
                return False
    return True


def color_bipartite(graph, s):
    """二部グラフを彩色する"""
    n = len(graph)
    col = [-1] * n
    col[s] = 0
    stack = [s]
    while stack:
        v = stack.pop()
        for nxt_v in graph[v]:
            if col[nxt_v] == -1:
                col[nxt_v] = col[v] ^ 1
                stack.append(nxt_v)
    return col


n, m = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]

graph = [set() for i in range(n)]
for a, b in info:
    a -= 1
    b -= 1
    graph[a].add(b)
    graph[b].add(a)

comp_graph = [[] for i in range(n)]
for a in range(n):
    for b in range(n):
        if b in graph[a] or a == b:
            continue
        comp_graph[a].append(b)


cnt0 = []
cnt1 = []
used = [False] * n
for i in range(n):
    if used[i]:
        continue
    used[i] = True
    if not is_bipartite(comp_graph, i):
        print(-1)
        return
    col = color_bipartite(comp_graph, i)
    cnt0.append(col.count(0))
    cnt1.append(col.count(1))

dp = [[False] * (n + 1) for i in range(len(cnt0) + 1)]
dp[0][0] = True
for i in range(len(cnt0)):
    wei0 = cnt0[i]
    wei1 = cnt1[i]
    for w in range(n + 1):
        if w + wei0 < n + 1:
            dp[i + 1][w + wei0] = (dp[i][w] or dp[i + 1][w + wei0])
        if w + wei1 < n + 1:
            dp[i + 1][w + wei1] = (dp[i][w] or dp[i + 1][w + wei1])

ans = 10 ** 18
for num in range(n + 1):
    if dp[-1][num]:
        c0 = num
        c1 = n - num
        res = c0 * (c0 - 1) // 2 + c1 * (c1 - 1) // 2
        ans = min(ans, res)
print(ans)
