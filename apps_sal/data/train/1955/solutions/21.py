from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self,n):
                self.p=list(range(n))
            def union(self,x,y):
                self.p[self.find(x)]=self.find(y)
            def find(self,x):
                if self.p[x] is not x:
                    self.p[x]=self.find(self.p[x])
                return self.p[x]
        uf,res,m=UF(len(s)),[],defaultdict(list)
        for x,y in pairs:
            uf.union(x,y)
        for i in range(len(s)):
            m[uf.find(i)].append(s[i])
        for i in m.keys():
            m[i].sort(reverse=True)
        for i in range(len(s)):
            res.append(m[uf.find(i)].pop())
        return ''.join(res)
