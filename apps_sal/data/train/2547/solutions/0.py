class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for arr in grid:
            for num in arr:
                if num < 0:
                    count +=1
        return count
