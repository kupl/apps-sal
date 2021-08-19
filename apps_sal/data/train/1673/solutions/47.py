class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        for i in range(1, n):
            for j in range(n):
                prevNonAdj = [arr[i - 1][k] for k in range(n) if k != j]
                arr[i][j] += min(prevNonAdj)
        return min(arr[n - 1])
