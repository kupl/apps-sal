from collections import deque
n, m = map(int, input().split())
p = list(map(int, input().split()))
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
v = [-1 for i in range(n)]
s = 0
for i in range(n):
    if v[i] != -1:
        continue
    s += 1
    v[i] = s
    d = deque([i])
    while len(d):
        x = d.popleft()
        for i in g[x]:
            if v[i] == -1:
                d.append(i)
                v[i] = s
ans = 0
for i in range(n):
    if v[i] == v[p[i] - 1]:
        ans += 1
print(ans)
