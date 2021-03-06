from collections import deque
(n, m) = map(int, input().split())
N = [0] * n
L = [list() for i in range(n)]
for i in range(m):
    (u, v, c) = map(int, input().split())
    L[~-u].append([~-v, c])
    L[~-v].append([~-u, c])
(N[0], Q) = (1, deque([0]))
while Q:
    u = Q.popleft()
    for (v, c) in L[u]:
        if N[v]:
            continue
        Q.append(v)
        if N[u] != c:
            N[v] = c
            continue
        for i in range(1, n + 1):
            if i != c:
                N[v] = i
                break
print(*N, sep='\n')
