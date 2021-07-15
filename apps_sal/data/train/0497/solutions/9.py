class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [0 for j in range(len(jobs))]
        
        for i in range(len(jobs)):
            if i == 0:
                inc_n = 0
            else:
                inc_n = dp[i-1]
            
            ind = self.find(jobs, jobs[i][0])
            if ind == -1:
                inc = jobs[i][2]
            else:
                inc = dp[ind] + jobs[i][2]
            dp[i] = max(inc, inc_n)
            
        print(dp)
        return dp[-1]
    
    def find(self, arr, val):
        l = 0
        r = len(arr) - 1
        ans = -1
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] > val:
                r = m - 1
            else:
                ans = m
                l = m + 1
                
        return ans
                

