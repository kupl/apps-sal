N, M = list(map(int, input().split()))
edges = [list([int(x) - 1 for x in input().split()]) for _ in range(M)]

adges = [[] for _ in range(N)]
for u, v, c in edges:
    adges[u].append([v, c])
    adges[v].append([u, c])

visited = [False] * N

cur = edges[0][0]
visited[cur] = True


Q = [cur]
use_edges = []
while Q:
    cur = Q.pop()
    for nex, label in adges[cur]:
        if visited[nex]:
            continue
        else:
            Q.append(nex)
            visited[nex] = True
            use_edges.append([cur, nex, label])


if all(v for v in visited):
    pass
else:
    print("No")
    return

ans = [-1] * N
adj_use = [[] for _ in range(N)]
for u, v, c in use_edges:
    adj_use[u].append([v, c])
    adj_use[v].append([u, c])


cur = None
for i in range(N):
    if len(adj_use[i]) == 1:
        cur = i
        break

for u, v, l in use_edges:
    if u == cur or v == cur:
        if l == 0:
            ans[cur] = 1
        else:
            ans[cur] = 0
        break
Q = [cur]

while Q:
    cur = Q.pop()
    for nex, label in adj_use[cur]:
        if ans[nex] != -1:
            continue
        else:
            Q.append(nex)
            if ans[cur] == label:
                ans[nex] = (label + 1) % N
            else:
                ans[nex] = label

for a in ans:
    print((a + 1))
