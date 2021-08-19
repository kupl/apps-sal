class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        (m, n) = (len(arr), len(arr[0]))
        for i in range(m - 1)[::-1]:
            for j in range(n):
                arr[i][j] += min((arr[i + 1][k] for k in range(n) if k != j))
        return min(arr[0])
