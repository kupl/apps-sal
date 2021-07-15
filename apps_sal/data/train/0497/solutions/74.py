import bisect
import numpy as np

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        X = list(zip(endTime,profit,startTime))
        s = sorted(X)
        end = [x for x,_,_ in s]
        prof = [x for _,x,_ in s]
        start = [x for _,_,x in s]

        p = [0] * (len(end))
        
        for i in range(len(end) -1,-1,-1):
            idx = bisect.bisect(end,start[i],lo =0,hi=i)
            p[i] = idx

        dp = [0] * (len(end) + 1)
        
        for i in range(1,len(end)+1):
            dp[i] = max(prof[i-1] + dp[p[i-1]], dp[i-1])
        
        print(dp)
        
        return max(dp)
        

        
            
            
            

