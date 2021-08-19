class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        m = {}
        new_start = []
        for (i, v) in enumerate(startTime):
            new_start.append((v, i))
            if v in m:
                m[v].append((endTime[i], profit[i]))
            else:
                m[v] = [(endTime[i], profit[i])]
        new_start = [(v, i) for (i, v) in enumerate(startTime)]
        new_start.sort()
        last = new_start[-1][0]
        dp = [0] * (last + 1)
        for v in reversed(range(last + 1)):
            if v not in m:
                dp[v] = dp[v + 1]
                continue
            maxi = -float('inf')
            for (end, profit) in m[v]:
                maxi = max(maxi, profit)
                if end < len(dp):
                    val = dp[end] + profit
                    maxi = max(maxi, val)
                if v + 1 < len(dp):
                    maxi = max(maxi, dp[v + 1])
            dp[v] = maxi
        return dp[0]
