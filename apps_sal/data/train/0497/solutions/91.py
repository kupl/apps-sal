class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for idx in range(len(startTime)):
            jobs.append([startTime[idx], endTime[idx], profit[idx]])
        jobs.sort(key=lambda x: x[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            idx = self.bs(dp, s)
            if dp[idx - 1][1] + p >= dp[-1][1]:
                dp.append([e, dp[idx - 1][1] + p])
        return dp[-1][1]

    def bs(self, arr, val):
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid][0] >= val:
                r = mid
            else:
                l = mid + 1
        return l if arr[l][0] > val else l + 1
