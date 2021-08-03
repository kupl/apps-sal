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
    for i, v in enumerate(p[1:], 1):
        res[v].append(i)
    return res


def check(L, Par, wri, even):
    for i in range(len(Par)):
        if wri[i] and (wri[i] % 2 == even[i]):
            return False

    inf = 10**9 + 7
    dpu = [w if w is not None else inf for w in wri]
    dpd = [w if w is not None else -inf for w in wri]
    for l in L[::-1][:-1]:
        if dpu[l] == inf:
            continue
        if dpd[l] > dpu[l]:
            return False
        p = Par[l]
        dpu[p] = min(dpu[p], dpu[l] + 1)
        dpd[p] = max(dpd[p], dpd[l] - 1)
    if dpd[root] > dpu[root]:
        return False
    ans = [None] * N
    ans[root] = wri[root]
    for l in L[1:]:
        p = Par[l]
        if ans[p] - 1 >= dpd[l]:
            ans[l] = ans[p] - 1
        else:
            ans[l] = ans[p] + 1
    return ans


N = int(readline())
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
K = int(readline())

VP = [tuple(map(lambda x: int(x), readline().split())) for _ in range(K)]
wri = [None] * N
for v, p in VP:
    wri[v - 1] = p

root = VP[0][0] - 1
Par = getpar(Edge, root)
L = topological_sort_tree(Edge, root)

even = [True] * N
even[root] = (wri[root] % 2 == 0)
for l in L[1:]:
    p = Par[l]
    even[l] = not even[p]
ans = check(L, Par, wri, even)
if ans == False:
    print('No')
else:
    print('Yes')
    print('\n'.join(map(str, ans)))
