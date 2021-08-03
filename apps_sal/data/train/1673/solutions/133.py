class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        for i in range(1, len(arr)):
            r = heapq.nsmallest(2, arr[i - 1])

            for j in range(len(arr[0])):
                arr[i][j] += r[1] if arr[i - 1][j] == r[0] else r[0]

        return min(arr[-1])
