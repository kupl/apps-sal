import bisect


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda t: (t[1], t[0], t[2]))
        dp = [(0, 0)]
        for start, end, profit in jobs:
            i = bisect.bisect_right(dp, (start, float('inf')))
            profit += dp[i - 1][1]
            if profit <= dp[-1][1]:
                continue

            if end == dp[-1][0]:
                dp[-1] = (end, profit)
            else:
                dp.append((end, profit))

        return dp[-1][1]
