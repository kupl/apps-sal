class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1,m+1)]
        
        ans = []
        for querie in queries:
            idx = P.index(querie)
            del P[idx]
            P = [querie] + P
            ans.append(idx)
            
        return ans

