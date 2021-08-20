class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        start = collections.defaultdict(list)
        for (i, time) in enumerate(startTime):
            start[time].append(i)
        dp = [0] * (max(endTime) + 1)
        for t in range(max(endTime) - 1, 0, -1):
            if t in start:
                for i in start[t]:
                    dp[t] = max(profit[i] + dp[endTime[i]], dp[t + 1], dp[t])
            else:
                dp[t] = dp[t + 1]
        return dp[1]
