class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        y = 0
        for row in grid:
            l = 0
            r = len(row)
            while l < r:
                mid = l + (r - l) // 2
                if row[mid] < 0:
                    r = mid
                else:
                    l = mid + 1
            y += len(row) - r
        return y
