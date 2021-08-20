class Solution:

    def jobScheduling(self, S: List[int], E: List[int], profit: List[int]) -> int:
        n = len(S)
        jobs = sorted([(S[i], E[i], profit[i]) for i in range(n)], key=lambda x: x[1])
        S = [jobs[i][0] for i in range(n)]
        E = [jobs[i][1] for i in range(n)]
        profit = [jobs[i][2] for i in range(n)]
        dp = [-1] * n
        dp[0] = (profit[0], E[0])
        for i in range(1, n):
            (prev_profit, endTime) = dp[i - 1]
            startTime = S[i]
            left = 0
            right = i - 1
            ans = profit[i]
            while left <= right:
                mid = (left + right) // 2
                if dp[mid][1] <= startTime:
                    ans = max(ans, profit[i] + dp[mid][0])
                    left = mid + 1
                else:
                    right = mid - 1
            if ans > prev_profit:
                dp[i] = (ans, E[i])
            else:
                dp[i] = dp[i - 1]
        return max([ele[0] for ele in dp])
