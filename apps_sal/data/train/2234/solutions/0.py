import sys
from collections import deque


def solve():
    sys.setrecursionlimit(10 ** 6)
    readline = sys.stdin.readline
    writelines = sys.stdout.writelines
    N = int(readline())
    G = [[] for i in range(N)]
    for i in range(N - 1):
        (u, v) = map(int, readline().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    S = []
    FS = [0] * N
    LS = [0] * N
    depth = [0] * N
    stk = [-1, 0]
    it = [0] * N
    while len(stk) > 1:
        v = stk[-1]
        i = it[v]
        if i == 0:
            FS[v] = len(S)
            depth[v] = len(stk)
        if i < len(G[v]) and G[v][i] == stk[-2]:
            it[v] += 1
            i += 1
        if i == len(G[v]):
            LS[v] = len(S)
            stk.pop()
        else:
            stk.append(G[v][i])
            it[v] += 1
        S.append(v)
    L = len(S)
    lg = [0] * (L + 1)
    for i in range(2, L + 1):
        lg[i] = lg[i >> 1] + 1
    st = [[L] * (L - (1 << i) + 1) for i in range(lg[L] + 1)]
    st[0][:] = S
    b = 1
    for i in range(lg[L]):
        st0 = st[i]
        st1 = st[i + 1]
        for j in range(L - (b << 1) + 1):
            st1[j] = st0[j] if depth[st0[j]] <= depth[st0[j + b]] else st0[j + b]
        b <<= 1
    INF = 10 ** 18
    ans = []
    Q = int(readline())
    G0 = [[]] * N
    P = [0] * N
    deg = [0] * N
    KS = [0] * N
    A = [0] * N
    B = [0] * N
    for t in range(Q):
        (k, *vs) = map(int, readline().split())
        for i in range(k):
            vs[i] -= 1
            KS[vs[i]] = 1
        vs.sort(key=FS.__getitem__)
        for i in range(k - 1):
            x = FS[vs[i]]
            y = FS[vs[i + 1]]
            l = lg[y - x + 1]
            w = st[l][x] if depth[st[l][x]] <= depth[st[l][y - (1 << l) + 1]] else st[l][y - (1 << l) + 1]
            vs.append(w)
        vs.sort(key=FS.__getitem__)
        stk = []
        prv = -1
        for v in vs:
            if v == prv:
                continue
            while stk and LS[stk[-1]] < FS[v]:
                stk.pop()
            if stk:
                G0[stk[-1]].append(v)
            G0[v] = []
            it[v] = 0
            stk.append(v)
            prv = v
        que = deque()
        prv = -1
        P[vs[0]] = -1
        for v in vs:
            if v == prv:
                continue
            for w in G0[v]:
                P[w] = v
            deg[v] = len(G0[v])
            if deg[v] == 0:
                que.append(v)
            prv = v
        while que:
            v = que.popleft()
            if KS[v]:
                a = 0
                for w in G0[v]:
                    ra = A[w]
                    rb = B[w]
                    if depth[v] + 1 < depth[w]:
                        a += min(ra, rb + 1)
                    else:
                        a += ra
                A[v] = INF
                B[v] = a
            else:
                a = 0
                b = c = INF
                for w in G0[v]:
                    ra = A[w]
                    rb = B[w]
                    (a, b, c) = (a + ra, min(a + rb, b + ra), min(b + rb, c + min(ra, rb)))
                A[v] = min(a, b + 1, c + 1)
                B[v] = b
            p = P[v]
            if p != -1:
                deg[p] -= 1
                if deg[p] == 0:
                    que.append(p)
        v = min(A[vs[0]], B[vs[0]])
        if v >= INF:
            ans.append('-1\n')
        else:
            ans.append('%d\n' % v)
        for v in vs:
            KS[v] = 0
    writelines(ans)


solve()
