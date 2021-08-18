
from collections import deque, defaultdict

chg = 10**6
n, m = map(int, input().split())
edges = defaultdict(set)
visited = defaultdict(set)
for i in range(m):
    p, q, c = map(int, input().split())
    edges[p + c * chg].add(q + c * chg)
    edges[q + c * chg].add(p + c * chg)
    edges[p].add(p + c * chg)
    edges[q].add(q + c * chg)
    edges[p + c * chg].add(p)
    edges[q + c * chg].add(q)
    visited[p] = False
    visited[q] = False
    visited[p + c * chg] = False
    visited[q + c * chg] = False

ans = float("inf")
que = deque()
que.append((1, 0))
while que:
    now, dist = que.popleft()
    if visited[now]:
        continue
    visited[now] = True
    if now == n:
        ans = dist
        break
    for to in edges[now]:
        if now < chg and to > chg:
            que.append((to, dist + 1))
        else:
            que.appendleft((to, dist))
if ans == float("inf"):
    print(-1)
else:
    print(ans)
