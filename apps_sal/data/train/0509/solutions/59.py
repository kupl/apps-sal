from collections import deque
(n, m) = [int(i) for i in input().split()]
g = [[] for _ in range(n)]
for _ in range(m):
    (u, v, c) = [int(i) - 1 for i in input().split()]
    g[u].append([v, c])
    g[v].append([u, c])
num = [0] * n
d = deque()
d.append(0)
label = [-1] * n
label[0] = 0
while d:
    a = d.pop()
    if num[a]:
        continue
    num[a] = 1
    for (u, c) in g[a]:
        if num[u]:
            continue
        if label[a] != c:
            label[u] = c
        elif c == 0:
            label[u] = 1
        else:
            label[u] = 0
        d.appendleft(u)
for i in range(n):
    label[i] = str(label[i] + 1)
print('\n'.join(label))
