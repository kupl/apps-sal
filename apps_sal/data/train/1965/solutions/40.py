class DSU:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[py] > self.rank[px]:
                self.parent[px] = py
            else:
                self.parent[px] = py
                self.rank[px] += 1
            return True
        

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsu1, dsu2 = DSU(n), DSU(n)
        ans = 0
        for t, u, v in edges:
            if t == 3:
                if not dsu1.union(u - 1, v - 1) or not dsu2.union(u - 1, v - 1):
                    ans += 1
        
        for t, u, v in edges:
            if t == 1 and not dsu1.union(u - 1, v - 1):
                ans += 1
            if t == 2 and not dsu2.union(u - 1, v - 1):
                ans += 1
        
        p1, p2 = dsu1.find(0), dsu2.find(0)
        for i in range(n):
            if p1 != dsu1.find(i) or p2 != dsu2.find(i):
                return -1
        return ans
