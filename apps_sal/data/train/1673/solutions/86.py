from heapq import nsmallest
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[0] * len(arr[0]) for _ in range(len(arr))]
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            min1, min2 = nsmallest(2, arr[i - 1])
            for j in range(len(arr[0])):
                if arr[i - 1][j] == min1:
                    arr[i][j] += min2
                else:
                    arr[i][j] += min1
        return min(arr[-1])
                

