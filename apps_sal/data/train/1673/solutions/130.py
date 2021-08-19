class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        def findMinOtherThanThis(nums):
            ret = list()
            (left, right) = ([0 for i in range(len(arr))], [0 for i in range(len(arr))])
            left_min = float('inf')
            for (idx, n) in enumerate(nums):
                left[idx] = left_min
                left_min = min(left_min, n)
            right_min = float('inf')
            for idx in range(len(nums) - 1, -1, -1):
                right[idx] = right_min
                right_min = min(right_min, nums[idx])
            for idx in range(len(nums)):
                ret.append(min(left[idx], right[idx]))
            return ret
        if not arr:
            return 0
        m = len(arr)
        n = len(arr[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i == m - 1:
                    dp[i][j] = arr[i][j]
                else:
                    dp[i][j] = arr[i][j] + dp[i + 1][j]
            dp[i] = findMinOtherThanThis(dp[i])
        return min(dp[0])
