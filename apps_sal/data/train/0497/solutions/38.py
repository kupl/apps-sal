class Job:

    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

    def __lt__(self, other):
        return (self.end, self.start, self.profit) < (other.end, other.start, other.profit)


class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        if n == 0:
            return 0
        arr = [Job(startTime[i], endTime[i], profit[i]) for i in range(n)]
        arr.sort()
        dp = [0 for x in range(n)]
        dp[0] = arr[0].profit
        for i in range(1, n):
            job = arr[i]
            cmax = job.profit
            le = self.binarySearch(arr, i, job.start)
            if 0 <= le < i:
                cmax += dp[le]
            dp[i] = max(dp[i - 1], cmax)
        return dp[-1]

    def binarySearch(self, arr, i, start):
        (s, e) = (0, i - 1)
        while s <= e:
            m = (s + e) // 2
            if arr[m].end > start:
                e = m - 1
            elif m == e or (0 <= m + 1 < i and arr[m + 1].end > start):
                return m
            else:
                s = m + 1
        return -(s + 1)
