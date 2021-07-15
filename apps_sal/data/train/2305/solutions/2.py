import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
VW = [[int(x)-1 for x in input().split()] for _ in range(N-1)]

"""
直径に次数1の頂点が生えている
"""

graph = [[] for _ in range(N)]
deg = [0] * N
for v,w in VW:
    graph[v].append(w)
    graph[w].append(v)
    deg[v] += 1
    deg[w] += 1

def dijkstra(start):
    INF = 10**10
    dist = [INF] * N
    q = [(start,0)]
    while q:
        qq = []
        for v,d in q:
            dist[v] = d
            for w in graph[v]:
                if dist[w] == INF:
                    qq.append((w,d+1))
        q = qq
    return dist

dist = dijkstra(0)
v = dist.index(max(dist))
dist = dijkstra(v)
w = dist.index(max(dist))
diag = v,w

def create_perm(start):
    arr = []
    v = start
    parent = None
    next_p = 1
    while True:
        n = 0
        next_v = None
        for w in graph[v]:
            if w == parent:
                continue
            if next_v is None or deg[next_v] < deg[w]:
                next_v = w
            if deg[w] == 1:
                n += 1
        if next_v is None:
            return arr + [next_p]
        if deg[next_v] == 1:
            n -= 1
        arr += list(range(next_p+1,next_p+n+1))
        arr.append(next_p)
        next_p += n+1
        parent = v
        v = next_v

P = create_perm(diag[1])

Q = create_perm(diag[0])

if len(P) != N:
    answer = -1
else:
    if P > Q:
        P = Q
    answer = ' '.join(map(str,P))
print(answer)


