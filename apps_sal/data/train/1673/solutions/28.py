class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        (m, n) = (len(arr), len(arr[0]))
        pre = arr[0][:]
        for i in range(1, m):
            dp = []
            for j in range(n):
                dp += [arr[i][j] + min((pre[k] for k in range(n) if k != j))]
            pre = dp
        return min(dp)
