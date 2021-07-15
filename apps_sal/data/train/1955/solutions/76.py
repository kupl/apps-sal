class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.count = n
        
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px==py:
            return
        self.count-=1
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
         # [[0,3],[1,2],[0,2]]
        for x,y in pairs:
            dsu.union(x,y)
        # [0,1,2,3]
        
        # Club everyone with the same parent
        if dsu.count == 1:
            return \"\".join(sorted(s))
        hm = collections.defaultdict(list)
        for i in range(n):
            hm[dsu.find(i)].append(s[i])
        for key in hm:
            hm[key].sort(reverse=True)
        res = []
        for i in range(n):
            res.append(hm[dsu.find(i)].pop())
        return \"\".join(res)
            
        
