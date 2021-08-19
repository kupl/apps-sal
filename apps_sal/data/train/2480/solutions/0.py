class Solution:

    def minCostToMoveChips(self, position: List[int]) -> int:
        d = {}
        a = 0
        b = 0
        for i in position:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d:
            if i % 2 == 0:
                a += d[i]
            else:
                b += d[i]
        return min(a, b)
