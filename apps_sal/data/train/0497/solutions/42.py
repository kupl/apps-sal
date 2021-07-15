class Solution:
     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def last_non_conflict(jobs, i):
            for j in range(i - 1, -1, -1):
                if jobs[j][1] <= jobs[i][0]:
                    return j
            return -1
        
        def recursive(jobs, l):
            if l == 1:
                return jobs[0][2]
            if l in dp:
                return dp[l]
            include_profit = jobs[l-1][2]
            i = last_non_conflict(jobs, l - 1)
            if i != -1:
                include_profit += recursive(jobs, i + 1)
            exclude_profit = recursive(jobs, l - 1)
            dp[l] = max(include_profit, exclude_profit)
            return dp[l]
        
        n = len(startTime)
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        jobs.sort(key=lambda x: x[1])
        dp = dict()
        return recursive(jobs, n)
