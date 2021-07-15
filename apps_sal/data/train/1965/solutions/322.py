class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0]*n
        self.count = 1
    def find(self, x):
        if x != self.parents[x]:
            # path compression, recursively
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        # find root parents
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            self.parents[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parents[px] = py
        else:
            # 如果相等，加rank
            self.parents[px] = py
            self.rank[py] += 1
        self.count += 1
        return True
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # undirected map -- redundant detection --> union find  
        uf1, uf2, ans = UnionFind(n), UnionFind(n), 0
\t\t
        for t, u, v in edges:
            if t != 3:
                continue
            if not uf1.union(u - 1, v - 1) or not uf2.union(u - 1, v - 1):
                ans += 1
        
        for t, u, v in edges:
            if t == 1 and not uf1.union(u - 1, v - 1):
                ans += 1
            elif t == 2 and not uf2.union(u - 1, v - 1):
                ans += 1
   
        return ans if uf1.count == n and uf2.count == n else -1
