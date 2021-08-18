from bisect import bisect_right


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        pair, N = sorted(enumerate(endTime), key=lambda tup: tup[1]), len(endTime)
        endTime, startTime, profit = [e for _, e in pair], [startTime[i] for i, _ in pair], [profit[i] for i, _ in pair]
        dp = [0] * (N + 1)
        for i, s in enumerate(startTime):
            j = bisect_right(endTime, s, 0, i) - 1
            dp[i] = max(dp[i - 1], dp[j] + profit[i])
        return dp[N - 1]
