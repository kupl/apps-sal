class UnionFind:
    
    def __init__(self, n):
        self.reps = [i for i in range(n)]
    
    def find(self, x):
        while x != self.reps[x]:
            self.reps[x] = self.reps[self.reps[x]]
            x = self.reps[x]
        return x
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.reps[x_root] = y_root
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        
        for i, j in pairs:
            uf.union(i, j)
            
        mp = collections.defaultdict(list)
        
        for i in range(len(s)):
            mp[uf.find(i)].append(s[i])
            
        for comp_id in mp.keys(): 
            mp[comp_id].sort(reverse=True)
        
        
        ret = []
        for i in range(len(s)): 
            ret.append(mp[uf.find(i)].pop())
        return \"\".join(ret)
        
