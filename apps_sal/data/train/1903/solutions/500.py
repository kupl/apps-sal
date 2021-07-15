import heapq
class Solution:
    def minCostConnectPoints_Prim(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        visited = set()
        visited.add(0)
        res = 0
        heap = c[0]
        
        heapq.heapify(heap)

        while len(visited)<n:
            d, j = heapq.heappop(heap)
            if j not in visited:
                visited.add(j)
                res += d
                for record in c[j]:
                    heapq.heappush(heap,record)
                    
        return res
    
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                edges.append((manhattan(points[i], points[j]), i, j))
        edges.sort()
        res = 0
        ds = DisjointSet(n)
        for cost, u, v in edges:
            if ds.find(u) != ds.find(v):
                ds.union(u,v)
                res += cost
        return res
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa==pb:
            return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa] 
    def find(self, p):
        if self.parent[p] == p:
            return p
        self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
