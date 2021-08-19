import heapq


class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        xm = [(0, -1), (0, -1)]
        for i in range(n):
            xm = heapq.nsmallest(2, [(x + xm[1][0], j) if j == xm[0][1] else (x + xm[0][0], j) for (j, x) in enumerate(arr[i])])
        return xm[0][0]
