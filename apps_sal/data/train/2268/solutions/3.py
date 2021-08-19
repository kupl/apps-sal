import sys
from itertools import chain
readline = sys.stdin.readline

# 非再帰


def scc(Edge):
    N = len(Edge)
    Edgeinv = [[] for _ in range(N)]
    for vn in range(N):
        for vf in Edge[vn]:
            Edgeinv[vf].append(vn)

    used = [False] * N
    dim = [len(Edge[i]) for i in range(N)]
    order = []
    for st in range(N):
        if not used[st]:
            stack = [st, 0]
            while stack:
                vn, i = stack[-2], stack[-1]
                if not i and used[vn]:
                    stack.pop()
                    stack.pop()
                else:
                    used[vn] = True
                    if i < dim[vn]:
                        stack[-1] += 1
                        stack.append(Edge[vn][i])
                        stack.append(0)
                    else:
                        stack.pop()
                        order.append(stack.pop())
    res = [None] * N
    used = [False] * N
    cnt = -1
    for st in order[::-1]:
        if not used[st]:
            cnt += 1
            stack = [st]
            res[st] = cnt
            used[st] = True
            while stack:
                vn = stack.pop()
                for vf in Edgeinv[vn]:
                    if not used[vf]:
                        used[vf] = True
                        res[vf] = cnt
                        stack.append(vf)
    M = cnt + 1
    components = [[] for _ in range(M)]
    for i in range(N):
        components[res[i]].append(i)
    tEdge = [[] for _ in range(M)]
    teset = set()
    for vn in range(N):
        tn = res[vn]
        for vf in Edge[vn]:
            tf = res[vf]
            if tn != tf and tn * M + tf not in teset:
                teset.add(tn * M + tf)
                tEdge[tn].append(tf)
    return res, components, tEdge


N = int(readline())
P = list([int(x) - 1 for x in readline().split()])

Edge = [[] for _ in range(N)]
for i in range(N):
    Edge[P[i]].append(i)

R, Com, _ = scc(Edge)

Lord = list(chain(*Com[::-1]))
val = [None] * N
for vn in Lord:
    if not R[vn]:
        break
    lvn = len(Edge[vn]) + 1
    res = [0] * lvn
    for vf in Edge[vn]:
        if val[vf] < lvn:
            res[val[vf]] += 1

    for k in range(lvn):
        if not res[k]:
            val[vn] = k
            break

st = Lord[-1]
lst = len(Edge[st]) + 2
res = [0] * lst
for vf in Edge[st]:
    if val[vf] is None:
        continue
    if val[vf] < lst:
        res[val[vf]] += 1
mc = []
for k in range(lst):
    if not res[k]:
        mc.append(k)

vn = st
Ls = []
while vn is not None:
    for vf in Edge[vn]:
        if R[vf]:
            continue
        if vf == st:
            vn = None
        else:
            Ls.append(vf)
            vn = vf

Ls.reverse()

ans = False
for idx in range(2):
    vc = val[:]
    vc[st] = mc[idx]
    for vn in Ls:
        lvn = len(Edge[vn]) + 1
        res = [0] * lvn
        for vf in Edge[vn]:
            if vc[vf] < lvn:
                res[vc[vf]] += 1

        for k in range(lvn):
            if not res[k]:
                vc[vn] = k
                break

    for vn in range(N):
        res = [False] * vc[vn]
        for vf in Edge[vn]:
            if vc[vn] == vc[vf]:
                break
            if vc[vf] < vc[vn]:
                res[vc[vf]] = True
        else:
            if not all(res):
                break
            continue
        break
    else:
        ans = True
    if ans:
        break
print(('POSSIBLE' if ans else 'IMPOSSIBLE'))
