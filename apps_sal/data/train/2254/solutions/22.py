from sys import stdin
input = stdin.readline
(n, q) = list(map(int, input().split()))
arr = [tuple(map(int, input().split())) for _ in range(q)]
adj = [[] for _ in range(n + 1)]
(curr, cnt, res, vis) = (0, 0, [], [])
for (t, v) in arr:
    if t == 1:
        adj[v].append(len(vis))
        vis.append(0)
        cnt += 1
    elif t == 2:
        for u in adj[v]:
            if not vis[u]:
                vis[u] = 1
                cnt -= 1
        adj[v] = []
    else:
        while v > curr:
            if not vis[curr]:
                vis[curr] = 1
                cnt -= 1
            curr += 1
    res.append(cnt)
print('\n'.join(map(str, res)))
