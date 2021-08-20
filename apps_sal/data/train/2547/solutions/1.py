class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for i in grid:
            for j in i:
                if j < 0:
                    counter += 1
        return counter
