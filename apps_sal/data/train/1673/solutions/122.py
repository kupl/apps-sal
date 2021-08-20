class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        rows = len(arr)
        for row in range(1, rows):
            nsmall_in_row = heapq.nsmallest(2, arr[row - 1])
            for col in range(0, rows):
                arr[row][col] += nsmall_in_row[1] if nsmall_in_row[0] == arr[row - 1][col] else nsmall_in_row[0]
        return min(arr[-1])
