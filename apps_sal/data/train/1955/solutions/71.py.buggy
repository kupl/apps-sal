class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self,n):
                self.p=list(range(n))
            def find(self,x):
                if x!=self.p[x]:
                    self.p[x]=self.find(self.p[x])
                return self.p[x]
            def union(self,x,y):
                self.p[self.find(x)]=self.find(y)
        d=defaultdict(list)
        uf=UF(len(s))
        ans=[]
        for x,y in pairs:
            uf.union(x,y)
        for i in range(len(s)):
            d[uf.find(i)].append(s[i])
        for key in d:
            d[key].sort(reverse=True)
        for i in range(len(s)):
            ans.append(d[uf.find(i)].pop())
        return \"\".join(ans)
    
