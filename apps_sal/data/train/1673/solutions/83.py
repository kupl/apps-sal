class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        # brute force recursive solution (TLE)
        # answer = float(\"inf\")
        # def helper(rowIdx, prevIdx, curr):
        #     nonlocal answer
        #     if rowIdx == len(arr):
        #         answer = min(answer, sum(curr))
        #         return
        #     row = arr[rowIdx]
        #     for i in range(len(row)):
        #         if rowIdx != 0 and i != prevIdx:
        #             curr.append(row[i])
        #             helper(rowIdx+1, i, curr)
        #             curr.pop()
        #         elif rowIdx == 0:
        #             curr.append(row[i])
        #             helper(rowIdx+1, i, curr)
        #             curr.pop()
        # helper(0, 0, [])
        # return answer

        # bottom-up DP solution
        dp = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
        for i in range(len(dp)):
            dp[0][i] = arr[0][i]

        for i in range(1, len(dp)):
            for j in range(len(dp[i])):
                if j == 0:  # left edge
                    dp[i][j] = min(arr[i][j] + dp[i - 1][k] for k in range(1, len(dp[i])))
                elif j == len(dp[i]) - 1:  # right edge
                    dp[i][j] = min(arr[i][j] + dp[i - 1][k] for k in range(len(dp[i]) - 1))
                else:  # in between
                    left_max = min(arr[i][j] + dp[i - 1][k] for k in range(j))
                    right_max = min(arr[i][j] + dp[i - 1][k] for k in range(j + 1, len(dp[i])))
                    dp[i][j] = min(left_max, right_max)

        return min(dp[-1])
