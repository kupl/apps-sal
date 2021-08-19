class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for r in grid:
            for i in range(len(r)):
                if r[i] < 0:
                    c += len(r) - i
                    break
        return c
