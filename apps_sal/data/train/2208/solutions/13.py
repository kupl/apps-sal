from collections import deque


def dfs(s, vis, items):
    ans = 0
    q = deque()
    q.append(s)
    vis[s] = True
    while len(q) > 0:
        u = q.popleft()
        for v in items[u]:
            if not vis[v]:
                vis[v] = True
                q.append(v)
                ans += 1
    return ans


n, k = map(int, input().split())
arr = [map(int, input().split()) for _ in range(k)]
items = [[] for _ in range(n + 1)]
for x, y in arr:
    items[x].append(y)
    items[y].append(x)
vis = [False for _ in range(n + 1)]
ans = k
for i, a in enumerate(items[1:]):
    if not vis[i]:
        ans -= dfs(i, vis, items)
print(ans)
