import numpy as np


class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        g = np.array(grid)
        g = list(np.concatenate(g))
        count = 0
        sum = 0
        for i in g:
            if sum + i < sum:
                count += 1
            sum = sum + i
        return count
