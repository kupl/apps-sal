class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        from collections import defaultdict
        times = sorted(set(startTime) | set(endTime))
        dp = [0] * len(times)
        time_id = {}
        for (i, x) in enumerate(times):
            time_id[x] = i
        start_id = defaultdict(list)
        for (i, x) in enumerate(startTime):
            start_id[x].append(i)
        for (i, x) in enumerate(times):
            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])
            for j in start_id[x]:
                et = endTime[j]
                dp[time_id[et]] = max(dp[time_id[et]], dp[i] + profit[j])
        return dp[-1]
