from collections import Counter
import sys
readline = sys.stdin.readline


def getpar(Edge, p):
    N = len(Edge)
    par = [0] * N
    par[0] = -1
    par[p] - 1
    stack = [p]
    visited = set([p])
    while stack:
        vn = stack.pop()
        for vf in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            stack.append(vf)
    return par


def topological_sort_tree(E, r):
    Q = [r]
    L = []
    visited = set([r])
    while Q:
        vn = Q.pop()
        L.append(vn)
        for vf in E[vn]:
            if vf not in visited:
                visited.add(vf)
                Q.append(vf)
    return L


def getcld(p):
    res = [[] for _ in range(len(p))]
    for (i, v) in enumerate(p[1:], 1):
        res[v].append(i)
    return res


N = int(readline())
We = list(map(int, readline().split()))
Edge = [[] for _ in range(N)]
Cost = Counter()
geta = N + 1
for _ in range(N - 1):
    (a, b, c) = list(map(int, readline().split()))
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
    Cost[b * geta + a] = c
    Cost[a * geta + b] = c
P = getpar(Edge, 0)
L = topological_sort_tree(Edge, 0)
C = getcld(P)
dp = [0] * N
candi = [[0, 0] for _ in range(N)]
ans = 0
for l in L[::-1][:-1]:
    dp[l] += We[l]
    p = P[l]
    k = dp[l] - Cost[l * geta + p]
    if k > 0:
        dp[p] = max(dp[p], k)
        candi[p].append(k)
    res = max(candi[l])
    candi[l].remove(res)
    ans = max(ans, We[l] + res + max(candi[l]))
res = max(candi[0])
candi[0].remove(res)
ans = max(ans, We[0] + res + max(candi[0]))
print(ans)
