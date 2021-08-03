from heapq import heapify, heappush, heappop


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        arr = stones
        n = len(stones)
        su = sum(arr)
        dp = [[0 for i in range(su + 1)] for j in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for j in range(1, n + 1):
            for i in range(1, su + 1):
                dp[j][i] = dp[j - 1][i]
                if i - arr[j - 1] >= 0:
                    dp[j][i] |= dp[j - 1][i - arr[j - 1]]

        diff = sys.maxsize

        # Find the largest j such that dp[n][j]
        # is true where j loops from sum/2 t0 0
        for j in range(su // 2, -1, -1):
            if dp[n][j] == True:
                diff = su - (2 * j)
                break

        return diff
