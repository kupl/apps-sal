class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        counter = 0
        for arr in grid:
            for num in arr:
                if num < 0:
                    counter += 1
        return counter
