# dp[i] :max profit if take the ith job
# dp[i] = max(0, dp[j] + profit[i] if endTime[j] <= startTime[i]) for j < i
# return max(dp)

# DP + Binary Search
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if len(startTime) != len(endTime) or len(startTime) != len(profit):
            return 0

        n = len(startTime)

        combined = []

        for i in range(n):
            combined.append((endTime[i], startTime[i], profit[i]))

        combined.sort()

        dp = [0] * n
        res = 0

        for i in range(n):
            end_i, start_i, profit_i = combined[i]
            dp[i] = max(dp[i - 1] if i > 0 else profit_i, profit_i)

            j = self.firstPosLargerThanTarget(combined, start_i, i)

            if j > 0:
                dp[i] = max(dp[j - 1] + profit_i, dp[i])

        return dp[-1]

    def firstPosLargerThanTarget(self, combined, target, end):
        left, right = 0, end

        while left + 1 < right:
            mid = (left + right) // 2

            if combined[mid][0] <= target:
                left = mid
            else:
                right = mid

        if combined[left][0] > target:
            return left

        return right
