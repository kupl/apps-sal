from collections import deque
n, m = map(int, input().split())
edge = [[] for i in range(n)]
for i in range(m):
    u, v, c = map(int, input().split())
    u-=1; v-=1
    edge[u].append((v, c))
    edge[v].append((u, c))

que = deque([0])
used = [0]*(n+1)
used[0]=1
while que:
    v = que.pop()
    for u, cost in edge[v]:
        if used[u]: continue
        if used[v]==cost:
            used[u] = cost%n+1
        else:
            used[u]=cost
        que.appendleft(u)
for i in range(n):
    print(used[i])
