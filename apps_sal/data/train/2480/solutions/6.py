class Solution:

    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        even = 0
        for pos in position:
            odd = odd + 1 if pos % 2 else odd
            even = even + 1 if not pos % 2 else even
        return min(odd, even)
