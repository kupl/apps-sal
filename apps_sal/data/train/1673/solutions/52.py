class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m = len(arr)
        n = len(arr[0])
        for i in range(1, m):
            for j in range(0, n):
                arr[i][j] += min([arr[i - 1][k] for k in range(0, n) if k != j])
        return min(arr[-1])
