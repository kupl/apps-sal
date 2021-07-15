class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        if len(queries)==0:
            return []
        P=[]
        for i in range(m):
            P.append(i+1)
        res=[]
        for i in queries:
            res.append(P.index(i))
            P.remove(i)
            P=[i]+P[:]
        return res
            

