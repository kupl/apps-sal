class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P=[i+1 for i in range(m)]
        res=[]
        for query in queries:
            idx=P.index(query)
            res.append(idx)
            pos=idx
            while(pos>0):
                P[pos]=P[pos-1]
                pos-=1
            P[0]=query
        return res
            
            

