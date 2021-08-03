class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [0] * (n + 1)

        for i, job in enumerate(jobs):
            s1, e1, p1 = job[0], job[1], job[2]
            dp[i + 1] = p1
            for j in range(i, -1, -1):
                if jobs[j][1] <= s1:
                    dp[i + 1] = max(dp[i], dp[j + 1] + job[2])
                    break
            dp[i + 1] = max(dp[i], dp[i + 1])
        return dp[-1]
