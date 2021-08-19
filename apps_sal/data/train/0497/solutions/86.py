class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        def bs(arr, l, r, target):
            while l <= r:
                m = l + (r - l) // 2
                if arr[m][0] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return r
        dp = [[0, 0]]
        for (e, s, p) in sorted(zip(endTime, startTime, profit)):
            idx = bs(dp, 0, len(dp) - 1, s)
            if p + dp[idx][1] > dp[-1][1]:
                dp.append([e, p + dp[idx][1]])
        return dp[-1][1]
