class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr:
            return 0
        rows, cols = len(arr), len(arr[0])

        for r in range(1, rows):
            for c in range(cols):
                val = float('inf')
                for x in range(cols):
                    if arr[r - 1][x] < val and x != c:
                        val = arr[r - 1][x]
                arr[r][c] += val
        return min(arr[-1])
