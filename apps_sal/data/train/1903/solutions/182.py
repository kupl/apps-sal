import heapq
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)
    
    def find(self, x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px==py:
            return False
        if self.rank[px]>self.rank[py]:
            self.parent[py] = px
        elif self.rank[px]<self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[px] += 1
        return True
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        if l == 1:
            return 0
        u = UnionFind(l)
        li = []
        c = 0
        ans = 0
        for i in range(l):
            for j in range(i+1,l):
                v = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                li.append((v,i,j))
        heapq.heapify(li)
        #li.sort(key = lambda x:x[2])
        while li:
            p = heapq.heappop(li)
            if u.find(p[1]) != u.find(p[2]):
                u.union(p[1],p[2])
                c = c + 1
                ans = ans + p[0]
            if c == l - 1:
                return ans
                

