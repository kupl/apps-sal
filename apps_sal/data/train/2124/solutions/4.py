from queue import Queue

def addEdge(s, t, flow):
    E[s].append((len(E[t]), t, flow))
    E[t].append((len(E[s])-1, s, 0))

def mkLevel():
    nonlocal src, des, E, lvl
    for i in range(n):
        lvl[i] = -1
    lvl[src] = 0
    
    q = Queue()
    q.put(src)
    while (not q.empty()):
        cur = q.get()
        for j in range(len(E[cur])):
            to = E[cur][j][1]
            if (lvl[to] < 0 and E[cur][j][2] > 0):
                lvl[to] = lvl[cur] + 1
                q.put(to)
                if (to == des):
                    return True
    return False

def extend(cur, lim):
    nonlocal des, E
    if (lim == 0 or cur == des):
        return lim
    flow = 0
    for j in range(len(E[cur])):
        if (flow >= lim):
            break
        to = E[cur][j][1]
        lim0 = min(lim-flow, E[cur][j][2])
        if (E[cur][j][2] > 0 and lvl[to] == lvl[cur] + 1):
            newf = extend(to, lim0)
            if (newf > 0):
                E[cur][j] = (E[cur][j][0], E[cur][j][1], E[cur][j][2] - newf)
                jj = E[cur][j][0]
                E[to][jj] = (E[to][jj][0], E[to][jj][1], E[to][jj][2] + newf)
                flow += newf
    if (flow == 0):
        lvl[cur] = -1
    return flow

def Dinic():
#    for i in range(len(E)):
#        print('i = {} : {}'.format(i, E[i]), flush = True)
    flow = 0
    newf = 0
    while (mkLevel()):
        newf = extend(src, INF)
        while (newf > 0):
            flow += newf
            newf = extend(src, INF)
    return flow

def check(mid):
    nonlocal E
    E = [[] for i in range(n)]
    for i in range(m):
        if (w[i] - bears * mid > 0):
            addEdge(u[i], v[i], bears)
        else:
            addEdge(u[i], v[i], int(w[i] / mid))
    return (Dinic() >= bears)

n,m,bears = list(map(int, input().split()))
#print(n, m, bears, flush = True)
INF = 0x3f3f3f3f
src = 0
des = n-1

lo = 0.0
hi = 0.0

u = [0 for i in range(m)]
v = [0 for i in range(m)]
w = [0 for i in range(m)]
for i in range(m):
    u[i],v[i],w[i] = list(map(int, input().split()))
    #print(u[i], v[i], w[i], flush = True)
    u[i] -= 1
    v[i] -= 1
    hi = max(hi, w[i])

E = [[] for i in range(n)]
lvl = [0 for i in range(n)]
for i in range(100):
    mid = (lo + hi) / 2
    #print('mid = {:.3f}'.format(mid), flush = True)
    if (check(mid)):
        lo = mid
    else:
        hi = mid

print('{:.10f}'.format(mid * bears))

