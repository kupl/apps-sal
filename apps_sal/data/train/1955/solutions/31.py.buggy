class DSU:
    def __init__(self, n):
        self.dsu = [i for i in range(n)]
        
    def find(self, x):
        if x == self.dsu[x]:
            return x
        self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.dsu[yr] = xr
        return
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        dsu = DSU(n)
        for x, y in pairs:
            dsu.union(x, y)
        groups = defaultdict(list)
        for i in range(n):
            key = dsu.find(i)
            groups[key].append(s[i])
        for k in groups:
            groups[k] = sorted(groups[k])
        ans = []
        for i in range(n):
            key = dsu.find(i)
            ans.append(groups[key].pop(0))
        return \"\".join(ans)
        
