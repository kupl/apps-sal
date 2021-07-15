class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[1])
        n = len(jobs)
        
        def binarySearchForLastDisjointInterval(interval: List[int]) -> int:
            s1, e1 = interval
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                s2, e2 = jobs[mid][0], jobs[mid][1]
                if s1 >= e2:
                    l = mid + 1
                else:
                    r = mid - 1
            return r
            
        def getLastDisjointIntervals() -> List[int]:
            last_disjoint_intervals = [None] * n
            for i in range(n):
                interval = [jobs[i][0], jobs[i][1]]
                last_disjoint_intervals[i] = binarySearchForLastDisjointInterval(interval)
            return last_disjoint_intervals
        
        last_disjoint_intervals = getLastDisjointIntervals()
        dp = [0] * n # dp[i] stores the maximum profit if we only consider the first (i+1) jobs
        dp[0] = jobs[0][2] # Can take the first job under any circumstance
        for i in range(1, n):
            # For a new job, we can either take this new job or don't take this new job
            # Consider not taking the new job
            profit_not_take = dp[i-1]
            # Consider taking the new job
            profit_take = jobs[i][2]
            j = last_disjoint_intervals[i]
            if j != -1:
                profit_take += dp[j]
            dp[i] = max(profit_not_take, profit_take)
        return dp[n-1]
