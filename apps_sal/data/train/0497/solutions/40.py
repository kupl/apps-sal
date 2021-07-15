class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        jobs.sort(key = lambda x: x[1])
        dp = [(0,0)]
        
        def find(time):
            n = len(dp)
            for i in range(n-1,-1,-1):
                if dp[i][0] <= time:
                    return dp[i][1]
        
        for j in jobs:
            dp.append((j[1],max(j[2] + find(j[0]), find(j[1]))))
        return dp[-1][1]
            
        

