class Solution:
    def minAreaRect(self, z: List[List[int]]) -> int:
        
        
        
        x=defaultdict(set)
        y=defaultdict(set)
        z.sort()
        #se= set(tuple(i) for i in z)
        for a,b in z:
            x[a].add(b)
            y[b].add(a)
        ans=inf
        l=len(z)
        for k in range(l):
            a,b=z[k]
            for m in range(k+1,l):
                c,d=z[m]
                if a<c:break
                for j in y[b].intersection(y[d]):
                    if j!=a:
                        ans= min(ans, abs(b-d)*abs(a-j))
        return ans if ans!=inf else 0
