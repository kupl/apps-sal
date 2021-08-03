import sys
readline = sys.stdin.readline


def parorder(Edge, p):
    N = len(Edge)
    par = [0] * N
    par[p] = -1
    stack = [p]
    order = []
    visited = set([p])
    ast = stack.append
    apo = order.append
    while stack:
        vn = stack.pop()
        apo(vn)
        for vf in Edge[vn]:
            if vf in visited:
                continue
            visited.add(vf)
            par[vf] = vn
            ast(vf)
    return par, order


def getcld(p):
    res = [[] for _ in range(len(p))]
    for i, v in enumerate(p[1:], 1):
        res[v].append(i)
    return res


N = int(readline())
root = None
Edge = [[] for _ in range(N)]
Cr = [None] * N
for a in range(N):
    b, c = list(map(int, readline().split()))
    b -= 1
    if b == -1:
        root = a
    else:
        Edge[a].append(b)
        Edge[b].append(a)
    Cr[a] = c

P, L = parorder(Edge, root)

dp = [0] * N

for l in L[:0:-1]:
    p = P[l]
    dp[p] += 1 + dp[l]

if any(d < c for d, c in zip(dp, Cr)):
    print('NO')
else:
    print('YES')
    A = [None] * N
    dp2 = [[] for _ in range(N)]
    for l in L[:0:-1]:
        p = P[l]
        dp2[l] = dp2[l][:Cr[l]] + [l] + dp2[l][Cr[l]:]
        dp2[p].extend(dp2[l])
    dp2[root] = dp2[root][:Cr[root]] + [root] + dp2[root][Cr[root]:]
    Ans = [None] * N
    for i in range(N):
        Ans[dp2[root][i]] = i + 1
    print(' '.join(map(str, Ans)))
