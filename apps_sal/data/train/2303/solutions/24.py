from collections import deque

N, M = map(int, input().split())
F_C_of_S = [{} for i in range(N)]
C_of_S = {}

parent = [-1] * M


def root(x):
    if (parent[x] < 0):
        return x
    else:
        parent[x] = y = root(parent[x])
        return y


def unite(x, y):
    px = root(x)
    py = root(y)
    if (px == py):
        return False
    if (parent[px] > parent[py]):
        px = root(y)
        py = root(x)
    parent[px] += parent[py]
    parent[py] = px
    return True


pqcs = []
for i in range(M):
    p, q, c = map(int, input().split())
    p -= 1
    q -= 1
    pqcs += [(p, q, c)]
    if not c in F_C_of_S[p]:
        F_C_of_S[p][c] = i
    else:
        unite(F_C_of_S[p][c], i)
    C_of_S.setdefault(p, set()).add(c)
    if not (c in F_C_of_S[q]):
        F_C_of_S[q][c] = i
    else:
        unite(F_C_of_S[q][c], i)
    C_of_S.setdefault(q, set()).add(c)

S_of_C = {}
for i in range(M):
    p, q, c = pqcs[i]
    c_set = S_of_C.setdefault(root(i), set())
    c_set.add(p)
    c_set.add(q)

Q = deque([(0, 0, 0)])
dist = [float('inf')] * N
dist[0] = 0

gdist = [float('inf')] * M

while Q:
    cost, v, flag = Q.popleft()
    if not (flag):
        for l in F_C_of_S[v].values():
            l = root(l)
            if (cost < gdist[l]):
                gdist[l] = cost
                Q.appendleft((cost, l, 1))
    else:
        for s in S_of_C[v]:
            if (cost + 1 < dist[s]):
                dist[s] = cost + 1
                Q.append((cost + 1, s, 0))

print(dist[N - 1] if dist[N - 1] < float('inf') else -1)
