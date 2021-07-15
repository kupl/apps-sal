class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class DSU:
            def __init__(self,n):
                self.n = n
                self.l = [i for i in range(n)]
            def get(self,c):
                if self.l[c] != c:
                    self.l[c] = self.get(self.l[c])
                return self.l[c]
            def merge(self,c,d):
                t1 = self.get(c)
                t2 = self.get(d)
                self.l[t1] = t2
                
        g = DSU(len(s))
        for a,b in pairs:
            g.merge(a,b)
        
        res = {}
        for i,c in enumerate(s):
            cl = g.get(i)
            if cl in res:
                res[cl][0].append(i)
                res[cl][1].append(c)
            else:
                res[cl] = [[i],[c]]
        
        result = ['']*len(s)
        for cl in res:
            l = sorted(res[cl][1],reverse=True)
            for i in res[cl][0]:
                result[i] = l.pop()
        return \"\".join(result)
