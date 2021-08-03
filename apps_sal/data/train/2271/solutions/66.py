from collections import deque
from collections import defaultdict
n, m = list(map(int, input().split()))
p = list(map(int, input().split()))
c = 0
for i in range(n):
    if p[i] == i + 1:
        c += 1
vis = [0] * n


def dfs(x):
    vis[x] = 1
    a.add(x + 1)

    di = deque()
    di.append(x)
    while di:
        now = di.popleft()
        for j in d[now]:
            if not vis[j]:
                vis[j] = 1
                a.add(j + 1)
                di.append(j)

    for u in d[x]:
        if vis[u] == 0:
            dfs(u)


d = defaultdict(list)
for i in range(m):
    a, b = list(map(int, input().split()))
    d[a - 1].append(b - 1)
    d[b - 1].append(a - 1)
ans = 0
for i in range(n):
    if vis[i] == 0:
        a = set()
        dfs(i)
        l = 0
        z = 0
        for j in a:
            if p[j - 1] in a:
                z += 1
            if p[j - 1] == j:
                l += 1
        ans = max(ans, c + z - l)
print(ans)
