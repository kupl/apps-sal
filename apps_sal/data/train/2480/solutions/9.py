class Solution:

    def minCostToMoveChips(self, p: List[int]) -> int:
        even = 0
        odd = 0
        for i in p:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)
