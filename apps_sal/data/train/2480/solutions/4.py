class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        l = [0, 0]
        for i in range(len(position)):
            if position[i] % 2 == 0:
                l[0] += 1
            else:
                l[1] += 1
        return min(l[0], l[1])
