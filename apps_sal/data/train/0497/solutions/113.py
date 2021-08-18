class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        arr = [(endTime[i], startTime[i], profit[i]) for i in range(n)]
        arr.sort()
        dp = [0 for x in range(n)]
        dp[0] = arr[0][2]
        for i in range(1, n):
            e, s, p = arr[i][0], arr[i][1], arr[i][2]
            bs, be = 0, i - 1
            ridx = -1
            while bs <= be:
                m = (bs + be) // 2
                if arr[m][0] > s:
                    be = m - 1
                else:
                    ridx = max(ridx, m)
                    bs = m + 1
            if ridx == -1:
                dp[i] = max(dp[i - 1], p)
            else:
                dp[i] = max(dp[i - 1], dp[ridx] + p)
        return max(dp)
