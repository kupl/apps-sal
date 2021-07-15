class Solution:
    def longestAwesome(self, s: str) -> int:
        res,mask=0,0
        n=len(s)
        memo=[n]*1024
        memo[0]=-1
        
        for i,ch in enumerate(s):
            mask^=1<<int(ch)
            
            res=max(res,i-memo[mask])
            
            for j in range(10):
                test_mask=mask^(1<<j)
                res=max(res,i-memo[test_mask])
            
            memo[mask]=min(memo[mask],i)
        return res

