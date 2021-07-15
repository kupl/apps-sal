class UnionFind:
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
        self.sz[yr] = self.sz[xr]
        return True

    def size(self, x):
        return self.sz[self.find(x)]
    
class Solution:
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n<=1:
            return 0
        distances = []
        db = dict()
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dis = (abs(x1-x2)+abs(y1-y2))
                distances.append( dis )

                if dis not in db:
                    db[dis] = []
                db[dis].append((i,j))
                
        
        heapq.heapify(distances)
        nodes = UnionFind(n)
        ret = []
        
        cost = 0
        while distances:
            # print(type(distances))
            # print(nodes)
            dis = heapq.heappop(distances)
            p1,p2 = db[dis].pop()
            if nodes.union(p1,p2):
                cost+=dis
        return cost

