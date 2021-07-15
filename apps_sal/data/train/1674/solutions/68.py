class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def dp(idx,M,people):
            if idx>=len(piles):
                return 0
            res=[]
            for X in range(1,2*M+1,1):
                res.append(dp(idx+X,max(M,X),1 if people==0 else 0)+people*sum(piles[idx:idx+X]))
            if people==1:
                return max(res)
            else:
                return min(res)
        return dp(0,1,1)
                

