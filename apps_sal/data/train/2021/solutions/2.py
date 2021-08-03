# in the name of god

from collections import defaultdict

n, m = list(map(int, input().strip().split()))

g = defaultdict(list)

for _ in range(m):
    u, v = list(map(int, input().strip().split()))
    g[u].append(v)
    g[v].append(u)

v1 = []
v2 = []

mark = [-1] * (n + 1)


def bfs(start):
    q = []
    q.append(start)
    mark[start] = 1
    v2.append(start)

    while q:
        v = q.pop(0)

        for u in g[v]:
            if mark[u] == -1:
                mark[u] = 1 - mark[v]
                q.append(u)
                if mark[u] == 0:
                    v1.append(u)
                else:
                    v2.append(u)

            elif mark[u] == mark[v]:
                return -1
    return 0


sw = False
for i in range(1, n + 1):
    if mark[i] == -1 and len(g[i]):
        res = bfs(i)

    try:
        if res == -1:
            sw = True
            break
    except:
        continue
if sw:
    print(-1)
else:
    print(len(v1))
    print(' '.join(str(x) for x in v1))
    print(len(v2))
    print(' '.join(str(x) for x in v2))
