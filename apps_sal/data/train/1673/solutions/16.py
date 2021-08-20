from heapq import nsmallest


class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        (m, n) = (len(arr), len(arr[0]))
        for i in range(m - 1)[::-1]:
            for j in range(n):
                ans = nsmallest(2, arr[i + 1])
                arr[i][j] += ans[0] if ans[0] != arr[i + 1][j] else ans[1]
        return min(arr[0])
