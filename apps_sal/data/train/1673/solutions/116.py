import heapq


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        copy = deepcopy(arr)

        for row in range(1, len(arr)):
            smallest = heapq.nsmallest(2, copy[row - 1])
            for col in range(len(arr[0])):
                copy[row][col] += smallest[0] if copy[row - 1][col] != smallest[0] else smallest[1]
        return min(copy[-1])
