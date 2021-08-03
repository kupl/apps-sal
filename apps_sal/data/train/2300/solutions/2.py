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


MOD = 10**9 + 7
limit = 1341398
p2 = [1] * limit
for i in range(1, limit):
    p2[i] = 2 * p2[i - 1] % MOD

N = int(readline())
P = [None] + list(map(int, readline().split()))
Edge = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    Edge[i].append(P[i])
    Edge[P[i]].append(i)
_, L = parorder(Edge, 0)
C = getcld(P)
dist = [0] * (N + 1)
for l in L[1:]:
    p = P[l]
    dist[l] = 1 + dist[p]
md = dist[:]
for l in L[:0:-1]:
    p = P[l]
    md[p] = max(md[p], md[l])

Ci = [None] * (N + 1)
for i in range(N + 1):
    if C[i]:
        res = -1
        cc = None
        for ci in C[i]:
            if md[ci] > res:
                res = md[ci]
                cc = ci
    Ci[i] = cc
ans = 0

res = [[0]]
val = [1] * (N + 1)
size = [1] * (N + 1)
used = [0] * (N + 1)
name = [None] * (N + 1)
mark = [None] * (N + 1)
while res:
    newres = []
    for a in res:
        ts = 1
        ks = 0
        ss = 0
        dic = []
        ctr = []

        for i in a:
            ts = ts * (p2[size[i]] - val[i]) % MOD
            ks = (ks + val[i] * pow(p2[size[i]] - val[i], MOD - 2, MOD)) % MOD
            ss += size[i]

            if not used[i]:
                used[i] = 1
                if C[i]:
                    dic.append(C[i])
                    if name[i] is None:
                        name[i] = Ci[i]
            if name[i] is not None:
                ctr.append(name[i])
        newres.extend(dic)
        if len(ctr) > 1:
            newres.append(ctr)
        for a0 in a:
            val[a0] = ts * ks % MOD
            size[a0] = ss
    ans = (ans + val[a0] * p2[N + 1 - size[a0]]) % MOD
    res = [nr[:] for nr in newres]
    # print(res)
print(ans)

"""
def merge(sz, vl):
    res = 0
    ts = 1
    ks = 0
    for s, v in zip(sz, vl):
        ts = ts*(p2[s] - v)%MOD
        ks = (ks + v*pow(p2[s] - v, MOD-2, MOD))%MOD
    return ts*ks%MOD



assert N < 2000

st = [0]
aa = 0
while st:
    size = [0]*(N+1)
    val = [0]*(N+1)
    cs = [[] for _ in range(N+1)]
    cv = [[] for _ in range(N+1)]
    
    nr = []
    for s in st:
        cs[s] = [1]
        cv[s] = [1]
        nr.extend(C[s])
    for l in L[::-1]:
        size[l] = sum(cs[l])
        val[l] = merge(cs[l], cv[l])
        if l:
            p = P[l]
            cs[p].append(size[l])
            cv[p].append(val[l])
    aa = (aa + val[0]*p2[N+1 - size[0]])%MOD
    st = nr[:]

print(aa)
"""
