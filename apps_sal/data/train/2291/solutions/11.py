n,*d = map(int,open(0).read().split())
zd = {di:i for i,di in enumerate(d)}
*sd, = sorted(d)
parent = [-1]*n
size = {i:1 for i in d}
dist = {i:0 for i in d}
ok = 1
for v in sd[n-1:0:-1]:
    p = v - n + 2*size[v]
    if p >= v:
        ok = 0
        break
    if p in zd:
        size[p] += size[v]
        dist[p] += dist[v]+size[v]
        parent[zd[v]] = zd[p]
    else:
        ok = 0
        break
if dist[sd[0]] != sd[0]: ok = 0
if ok:
    for i,pi in enumerate(parent):
        if pi != -1: print(i+1,pi+1)
else:
    print(-1)
