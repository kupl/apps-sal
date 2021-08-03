class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m, n = len(arr), len(arr[0])
        for i in range(1, m):
            for j in range(n):
                m0, m1 = heapq.nsmallest(2, arr[i - 1])
                arr[i][j] += m0 if arr[i - 1][j] != m0 else m1

        return min(arr[-1])
