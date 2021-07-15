#[Runtime: 584 ms, faster than 74.95%] DP, BinarySearch
#O(NlogN)
#sort by endtime, iterate each job from earlier-end to latest-end
#f(i): the maximum profit if we can take job[0~i]
#f(-1) = 0
#f(i) = max{ f(i-1), f(j) + profit[i] } for first j s.t. endTime[j] <= startTime[i]
from bisect import bisect_right
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        pair, N = sorted(enumerate(endTime), key=lambda tup: tup[1]), len(endTime)
        endTime, startTime, profit = [e for _, e in pair], [startTime[i] for i, _ in pair], [profit[i] for i, _ in pair]
        dp = [0] * (N + 1)
        for i, s in enumerate(startTime):
            j = bisect_right(endTime, s, 0, i) - 1 #search in endTime[0~i-1]
            dp[i] = max(dp[i-1], dp[j] + profit[i]) #j=-1 if not found, and dp[-1] is 0
        return dp[N-1]
