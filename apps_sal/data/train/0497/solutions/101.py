class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        line = list(zip(startTime, endTime, profit))
        line.sort(key=lambda x: x[1])
        dp = [0] * n
        dp[0] = line[0][2]
        for i in range(n):
            prev_profit = 0
            (left, right) = (0, i - 1)
            while left <= right:
                mid = (left + right) // 2
                if line[i][0] < line[mid][1]:
                    right = mid - 1
                else:
                    prev_profit = dp[mid]
                    left = mid + 1
            dp[i] = max(dp[i - 1], prev_profit + line[i][2])
        return dp[-1]
