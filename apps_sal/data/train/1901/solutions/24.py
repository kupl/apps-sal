from collections import defaultdict, Counter
class Solution:
    def find(self, j):
        if self.d[j] == j:
            return j
        
        self.d[j] = self.find(self.d[j])
        return self.d[j]
    
    def union(self, ij1, ij2):
        i1 = self.find(ij1)
        i2 = self.find(ij2)
        if i1 == i2:
            return
        
        if self.rank[i2] > self.rank[i1]:
            self.d[i1] = i2
            # self.rank[i2] = self.rank[i1] + 1
        else:
            if self.rank[i1] >= self.rank[i2]:
                self.d[i2] = i1
            self.rank[i1] += 1
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.rank, self.d = {}, {}
        self.z = []
        self.res = 1
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == 1:
                    self.d[(r, c)] = (r, c)
                    self.rank[(r, c)] = 0
                if col == 0:
                    self.z.append((r, c))
                    
        for a, b in list(self.d.keys()):
            search = [(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)]
            for c, d in search:
                if 0 <= c < len(grid) and 0 <= d < len(grid[0]) and grid[c][d] == 1:
                    self.union((a, b), (c, d))
        for key in list(self.d.keys()):
            self.find(key)
        cc = Counter(list(self.d.values()))
        print(('cc ', cc))
        
        print(('d ', self.d))
        print(('rank', self.rank))
        if cc:
            self.res = max(cc.values())
        for a, b in self.z:
            search = [(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)]
            total = {}
            for c, d in search:
                if 0 <= c < len(grid) and 0 <= d < len(grid[0]) and grid[c][d] == 1:
                    e, f = self.d[(c, d)]
                    total[(e, f)] = cc[(e, f)]
            print(('total ', total))
            s = sum(total.values())
            self.res = max(self.res, s + 1)
            
        return self.res

