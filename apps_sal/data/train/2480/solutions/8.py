class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = len([p for p in position if p % 2])
        return min(odd, len(position) - odd)
