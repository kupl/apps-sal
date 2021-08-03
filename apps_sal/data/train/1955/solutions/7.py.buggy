class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px==py:
            return
        if self.rank[px]>self.rank[py]:
            self.parent[py] = px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px]=py
            self.rank[py]+=self.rank[x]
        
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        dsu = DSU(n)
        for x,y in pairs:
            dsu.union(x,y)
        # Club everyone with the same parent
        hm = collections.defaultdict(list)
        for i in range(n):
            hm[dsu.find(i)].append(s[i])
        for key in hm:
            hm[key].sort()
        res = []
        for i in range(n):
            res.append(hm[dsu.find(i)].pop(0))
        return \"\".join(res)
            
        
