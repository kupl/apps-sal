

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        n = len(startTime)
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        jobs.sort(key=lambda x: x[1])
        dp = [0] * (n + 1)

        for i in range(n):
            dp[i + 1] = dp[i]
            l = 0
            r = i - 1
            while l <= r:
                mid = (l + r) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    l = mid + 1
                else:
                    r = mid - 1
            dp[i + 1] = max(dp[i + 1], dp[l] + jobs[i][2])
        return dp[n]
