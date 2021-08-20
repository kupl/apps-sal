class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        ct = 0
        for i in grid:
            for j in i:
                if j < 0:
                    ct += 1
        return ct
