class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        dp = [0] * n
        dp[n - 1] = jobs[n - 1][2]
        for i in range(n - 2, -1, -1):
            dp[i] = max(jobs[i][2], dp[i + 1])
            for j in range(i + 1, n):
                if jobs[i][1] <= jobs[j][0]:
                    dp[i] = max(dp[i], jobs[i][2] + dp[j])
                    break
        print(jobs)
        print(dp)
        return dp[0]
