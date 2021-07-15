class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return len([c for r in grid for c in r if c<0])
