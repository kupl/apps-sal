from collections import defaultdict


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        times = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        n = len(endTime)
        dp = [(0, 0)]

        def bsearch(arr, target):
            start, end = 0, len(arr) - 1
            while start < end:
                mid = (end - start) // 2 + start
                if arr[mid][0] == target:
                    return mid
                elif arr[mid][0] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return start if target >= arr[start][0] else start - 1

        for i in range(1, n + 1):
            start, end, p = times[i - 1]
            last_start = bsearch(dp, start)
            if len(dp) > last_start >= 0:
                dp.append((end, max(dp[last_start][1] + p, dp[-1][1])))
            else:
                dp.append((end, p))
        return dp[n][1]
