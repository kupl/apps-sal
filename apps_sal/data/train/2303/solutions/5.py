from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


(N, M) = map(int, input().split())
X = []
C = [set() for _ in range(N)]
for _ in range(M):
    (p, q, c) = [int(a) - 1 for a in input().split()]
    X.append((p, q, c))
    C[p].add(c)
    C[q].add(c)
for (i, c) in enumerate(C):
    C[i] = list(c)
I = [N]
D = [{} for _ in range(N)]
for (i, c) in enumerate(C):
    for (j, a) in enumerate(c):
        D[i][a] = I[-1] + j
    I.append(I[-1] + len(c))
T = I[-1]
E = [[] for _ in range(T)]
for (p, q, c) in X:
    E[D[p][c]].append((D[q][c], 0))
    E[D[q][c]].append((D[p][c], 0))
for (i, c) in enumerate(C):
    for (j, a) in enumerate(c):
        E[i].append((D[i][a], 1))
        E[D[i][a]].append((i, 1))


def BFS01(n, E, i0=0):
    Q = deque([i0])
    D = [-1] * n
    D[i0] = 0
    while Q:
        x = Q.popleft()
        for (y, w) in E[x]:
            if w:
                if D[y] == -1:
                    D[y] = D[x] + 1
                    Q.append(y)
            elif D[y] == -1 or D[y] < D[x]:
                D[y] = D[x]
                Q.appendleft(y)
    return D


D = BFS01(T, E, 0)
print(D[N - 1] // 2)
