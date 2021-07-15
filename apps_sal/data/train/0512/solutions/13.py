import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
 
INF = 10**6
 
class RMQ:
    def __init__(self, a):
        self.n = len(a)
        self.size = 2**(self.n - 1).bit_length()
        self.data = [(INF, INF) for _ in range(2*self.size-1)]
        self.initialize(a)
 
    # Initialize data
    def initialize(self, a):
        for i in range(self.n):
            self.data[self.size + i - 1] = a[i][:]
        for i in range(self.size-2, -1, -1):
            self.data[i] = min(self.data[i*2 + 1], self.data[i*2 + 2])[:]
    
    # Update ak as x
    def update(self, k, x):
        k += self.size - 1
        self.data[k] = x
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = min(self.data[2*k+1], self.data[2*k+2])[:]
    
    # Min value in [l, r)
    def query(self, l, r):
        L = l + self.size; R = r + self.size
        s = (INF, INF)
        while L < R:
            if R & 1:
                R -= 1
                s = min(s, self.data[R-1])[:]
            if L & 1:
                s = min(s, self.data[L-1])[:]
                L += 1
            L >>= 1; R >>= 1
        return s
 
class LCA:
    def __init__(self, edge, root):
        self.itr = 0
        self.edge = edge[:]
        self.path = [0] * (2*n-1)
        self.depth = [0] * (2*n-1)
        self.color = [0] * (2*n-1)
        self.weight = [0] * (2*n-1)
        self.index = [0] * n
        self.euler_tour(-1, root, 0, 0, 0, 0)
        dat = list(zip(self.depth, self.path))
        self.rmq = RMQ(dat)
    
    # Lowest ancestor of u, v
    def get_lca(self, u, v):
        l, r = self.index[u], self.index[v]
        if l > r:
            l, r = r, l
        return self.rmq.query(l, r+1)[1]
    
    def euler_tour(self, prev, v, d, k, c, w):
        self.index[v] = k
        self.path[self.itr] = v
        self.depth[self.itr] = d
        self.color[self.itr] = c
        self.weight[self.itr] = w
        self.itr += 1
        k += 1
        for dest, c, w in self.edge[v]:
            if prev == dest:
                continue
            k = self.euler_tour(v, dest, d + 1, k, c, w)
            self.path[self.itr] = v
            self.depth[self.itr] = d
            self.color[self.itr] = -c
            self.weight[self.itr] = -w
            self.itr += 1
            k += 1
        return k
        
n, q = [int(item) for item in input().split()] 
edge = [[] for _ in range(n)]
 
for _ in range(n-1):
    u, v, c, w = [int(item) for item in input().split()]
    u -= 1; v -= 1
    edge[u].append((v, c, w))
    edge[v].append((u, c, w))
 
lca = LCA(edge, 0)
memo = [dict() for _ in range(n)]
lca_memo = dict()
 
query = []
for _ in range(q):
    x, y, u, v = [int(item) for item in input().split()]
    u -= 1; v -= 1
    if u > v:
        u, v = v, u
    if (u, v) in lca_memo:
        ca = lca_memo[(u, v)]
    else:
        ca = lca.get_lca(u, v)
        lca_memo[(u, v)] = ca
    memo[u][x] = None
    memo[v][x] = None
    memo[ca][x] = None
    query.append((x, y, ca, u, v))
 
colors = [0] * n
c_depth = [0] * n
depth = 0
for p, c, w in zip(lca.path[1:], lca.color[1:], lca.weight[1:]):
    color = abs(c)
    if c < 0:
        colors[color] -= 1
    else:
        colors[color] += 1
    c_depth[color] += w
    depth += w
 
    for key in memo[p].keys():
        if memo[p][key] != None:
            break
        memo[p][key] = (colors[key], c_depth[key])
    memo[p][0] = depth 
 
ans = []
for x, y, ca, u, v in query:
    # Calc basic distance
    val = memo[u][0] + memo[v][0] - memo[ca][0] * 2
    # Append color diff
    val += (memo[v][x][0] + memo[u][x][0] - memo[ca][x][0] * 2) * y 
    val -= (memo[v][x][1] + memo[u][x][1] - memo[ca][x][1] * 2)
    ans.append(val)
print("\n".join(map(str,ans)))
