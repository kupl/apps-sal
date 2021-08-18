
from collections import deque

n, m = map(int, input().split())

N = [0] * n
L = [[] for _ in range(n)]
for i in range(m):
    u, v, c = map(int, input().split())
    L[u - 1].append((v - 1, c))
    L[v - 1].append((u - 1, c))

N[0] = 1
Q = deque([0])
while Q:
    u = Q.popleft()
    for v, c in L[u]:
        if N[v]:
            continue
        Q.append(v)
        if N[u] != c:
            N[v] = c
        else:
            if c != 1:
                N[v] = 1
            else:
                N[v] = 2

print(*N, sep='\n')
