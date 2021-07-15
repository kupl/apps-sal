class DSU:
    
    def __init__(self, N):
        self.par = list(range(N))
        self.sz = [1] * N
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.sz[x] < self.sz[y]:
            x, y = y, x
        self.sz[x] += self.sz[y]
        self.par[y] = x
        return True
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        dsu = DSU(N)
        for a, b in pairs:
            dsu.union(a, b)
        s = list(s)
        components = [[] for i in range(N)]
        for i in range(N):
            components[dsu.find(i)].append(i)
        for i in range(N):
            chars = [s[j] for j in components[i]]
            chars.sort()
            for j, v in enumerate(components[i]):
                s[v] = chars[j]
        
        return \"\".join(s)
        
