'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        #distance = collections.defaultdict(list)
        edges = []
        
        def distance(point1, points):
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])
        
        for i,point1 in enumerate(points):
            for j, point2 in enumerate(points[i+1:]):
                edges.append((i,j+i+1, distance(point1,point2)))

        edges = sorted(edges, key = lambda x: x[2])
        
        union = list(range(n))
        rank = [0]*n
        
        def find(x):
            if union[x]!=x:
                union[x] = find(union[x])
            return union[x]
        
        def connect(x, y):
            xr, yr = find(x), find(y)
            if rank[xr] > rank[yr]:           
                union[yr] = xr
                rank[xr] += rank[yr]
            else:
                union[xr] = yr
                rank[yr] += xr

        result= 0
        times = 0
        while(edges and times < n):
            p1, p2, dis = edges.pop(0)    
            if find(p1)!=find(p2):
                connect(p1, p2)
                result += dis
                times +=1 
        return result
'''


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    # make a and b part of the same component
    # union by rank optimization
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]

    # find the representative of the
    # path compression optimization
    def find(self, a):
        if self.parent[a] == a:
            return a

        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        # sort based on cost (i.e. distance)
        edges.sort()

        # using Kruskal's algorithm to find the cost of Minimum Spanning Tree
        res = 0
        ds = DisjointSet(n)
        for cost, u, v in edges:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                res += cost

        return res
