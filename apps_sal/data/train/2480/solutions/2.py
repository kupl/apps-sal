from collections import Counter


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count_e = count_o = 0
        for pos in position:
            if pos % 2 == 0:
                count_e += 1
            else:
                count_o += 1

        return min(count_e, count_o)
