import sys
readline = sys.stdin.readline

def parorder(Edge, p):
    N = len(Edge)
    par = [0]*N
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
 
 


T = int(readline())
Ans = ['Bob']*T
for qu in range(T):
    N, fa, fb, da, db = map(int, readline().split())
    fa -= 1
    fb -= 1
    Edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, readline().split())
        a -= 1
        b -= 1
        Edge[a].append(b)
        Edge[b].append(a)
    
    if 2*da >= db:
        Ans[qu] = 'Alice'
        continue
    
    stack = [fa]
    dist = [0]*N
    used = set([fa])
    while stack:
        vn = stack.pop()
        for vf in Edge[vn]:
            if vf not in used:
                used.add(vf)
                dist[vf] = dist[vn] + 1
                stack.append(vf)
    if dist[fb] <= da:
        Ans[qu] = 'Alice'
        continue
    
    left = dist.index(max(dist))
    stack = [left]
    dist = [0]*N
    used = set([left])
    while stack:
        vn = stack.pop()
        for vf in Edge[vn]:
            if vf not in used:
                used.add(vf)
                dist[vf] = dist[vn] + 1
                stack.append(vf)
    
    D = max(dist)
    if 2*da >= D:
        Ans[qu] = 'Alice'




print('\n'.join(Ans))
