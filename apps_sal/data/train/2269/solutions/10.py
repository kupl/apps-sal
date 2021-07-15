from collections import Counter
import numpy as np

class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0]*size
    
    def find(self, x):
        stack = []
        parent = self.parent
        while parent[x] != x:
            stack.append(x)
            x = parent[x]
        for y in stack:
            parent[y] = x
        return x

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        
        if self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        elif self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif xr != yr:
            self.parent[yr] = xr
            self.rank[xr] += 1

def check_bipartiteness(n_vertices, edges):
    ds = DisjointSet(2*n_vertices)

    for a,b in edges:
        ds.union(a, b+n_vertices)
        ds.union(b, a+n_vertices)
    
    next_color = 0
    color = [-1]*(2*n_vertices)
    for v in range(n_vertices):
        ra = ds.find(v)
        rb = ds.find(v+n_vertices)
        if ra == rb:
            return None
        if color[ra] < 0:
            color[ra] = next_color
            color[rb] = next_color+1
            next_color += 2
        color[v] = color[ra]
        color[v+n_vertices] = color[rb]
    return color[:n_vertices]



n,m = list(map(int,input().split()))

mat = [[True]*t for t in range(n)]

for _ in range(m):
    a,b = list(map(int,input().split()))
    if a < b:
        a,b = b,a
    mat[a-1][b-1] = False

edges = ((a,b) for a in range(n) for b in range(a) if mat[a][b])

colors = check_bipartiteness(n, edges)
if colors is None:
    print((-1))
    return

cnt = Counter(colors)
dp = np.zeros(n,dtype=bool)
dp[0] = True

for i in range(n):
    a,b = cnt[i*2],cnt[i*2+1]
    if a == 0 and b == 0:
        break
    d = abs(a-b)
    if d == 0:
        continue
    ndp = np.zeros(n,dtype=bool)
    ndp[d:] = dp[:-d]
    ndp[:-d] |= dp[d:]
    ndp[:d] |= dp[d-1::-1]
    dp = ndp
x = list(dp).index(True)

a = (n-x)//2
b = n-a

print((a*(a-1)//2 + b*(b-1)//2))

