n, ne = map(int, input().split())
tr = [[] for __ in range(n)]
for __ in range(ne):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    tr[u].append(v)
    tr[v].append(u)

visited = [0] * n
r = 0
for i in range(n):
    if visited[i]: continue 
    q = [i]; visited[i] = 1
    for u in q:
        for v in tr[u]:
            if not visited[v]:
                visited[v] = 1
                q.append(v); r += 1
print(ne - r)
