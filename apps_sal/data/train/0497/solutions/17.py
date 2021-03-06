class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        l = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        l = sorted(l, key=lambda x: x[1])
        ma = 0

        def binarysearch(x):
            left = 0
            right = x
            while left < right:
                mid = (left + right) // 2
                if l[mid][1] <= l[x][0]:
                    if l[mid + 1][1] <= l[x][0]:
                        left = mid + 1
                    else:
                        return mid
                else:
                    right = mid - 1
            return left
        dp = [0] * len(startTime)
        for i in range(len(startTime)):
            dp[i] = max(dp[i - 1], l[i][2])
            p = binarysearch(i)
            if l[p][1] <= l[i][0]:
                dp[i] = max(dp[i], dp[p] + l[i][2])
        return dp[-1]
