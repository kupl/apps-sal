from collections import deque
n = int(input())
graph = [[] for i in range(n)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
distfrom1 = [-1] * n
distfromn = [-1] * n
distfrom1[0] = 0
distfromn[n - 1] = 0
d = deque([0])
while d:
    v = d.popleft()
    for i in graph[v]:
        if distfrom1[i] != -1:
            continue
        distfrom1[i] = distfrom1[v] + 1
        d.append(i)
d.append(n - 1)
while d:
    v = d.popleft()
    for i in graph[v]:
        if distfromn[i] != -1:
            continue
        distfromn[i] = distfromn[v] + 1
        d.append(i)
F = 0
for i in range(n):
    if distfrom1[i] <= distfromn[i]:
        F += 1
if F > n - F:
    print('Fennec')
else:
    print('Snuke')
