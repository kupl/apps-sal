class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        n = len(profit)
        for i in range(n):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort(key=lambda x: x[1])

        dp = [0 for i in range(n + 1)]
        for i in range(n):
            start = jobs[i][0]
            prof = 0
            for j in reversed(range(i)):
                if jobs[j][1] <= start:
                    prof = dp[j + 1]
                    break
            dp[i + 1] = max(dp[i], prof + jobs[i][2])
        # print(dp)
        return dp[n]
