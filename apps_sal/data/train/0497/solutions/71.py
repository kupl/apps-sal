# dynamic programming + binary search
import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime,endTime,profit))
        startTime = sorted(startTime)
        dp = [-1]*len(jobs)
        
        def helper(index):
            if index == len(jobs):
                return 0
            
            if dp[index] != -1:
                return dp[index]
            
            currEnd, currProfit = jobs[index][1],jobs[index][2]
            
            newIdx = bisect.bisect_left(startTime,currEnd)
            
            currRes = max(currProfit + helper(newIdx), helper(index+1))
            
            ans = max(dp[-1],currRes)
            
            dp[index] = ans
            
            return ans
        
        return helper(0)
