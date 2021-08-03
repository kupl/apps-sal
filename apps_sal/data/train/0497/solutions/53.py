from collections import defaultdict


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        time_dict = defaultdict(list)

        for start, end, p in zip(startTime, endTime, profit):
            time_dict[end].append((start, p))

        n = max(endTime)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i not in time_dict:
                dp[i] = dp[i - 1]
                continue
            for start, profit in time_dict[i]:
                curr_p = dp[start] + profit
                dp[i] = max(curr_p, dp[i], dp[i - 1])
        return dp[n]
