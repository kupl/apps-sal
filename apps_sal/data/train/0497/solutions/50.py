class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(endTime)
        endidx = defaultdict(list)
        maxt = 0
        for i, t in enumerate(endTime):
            endidx[t].append(i)
            maxt = max(maxt, t)
        dp = [0] * (maxt + 1)
        for t in range(1, maxt + 1):
            if t not in endidx:
                dp[t] = dp[t - 1]
            else:
                cur = dp[t - 1]
                for i in endidx[t]:
                    cur = max(cur, dp[startTime[i]] + profit[i])
                dp[t] = cur
        return dp[-1]
