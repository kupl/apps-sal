class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    
    def find(self, x):
        if(self.p[x] != x):
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr
        
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        dsu = DSU(N)
        
        for x, y in pairs:
            dsu.union(x, y)
            
        dic = collections.defaultdict(list)
        for i in range(N):
            k = dsu.find(i)
            dic[k].append(i)
        
        res = [' ']*N
        for v in dic.values():
            for i, j in zip(v, sorted(v, key=lambda idx:s[idx])):
                res[i] = s[j]
        return \"\".join(res)
