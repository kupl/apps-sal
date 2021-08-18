from collections import defaultdict


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        finish = defaultdict(list)
        for i, j, k in zip(startTime, endTime, profit):
            finish[j].append((i, k))

        nn = max(endTime)
        dp = [0] * (nn + 1)
        for i in range(2, nn + 1):
            if i in finish:
                for j in finish[i]:
                    dp[i] = max(dp[i - 1], dp[j[0]] + j[1], dp[i])
            else:
                dp[i] = dp[i - 1]
        return dp[nn]
