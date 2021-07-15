class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        position.sort()
        mn = float('inf')
        def getTo(index,p):
            res = 0
            for i in range(len(position)):
                res += abs(p - position[i])%2
            return res
        for i in range(len(position)):
            mn = min(mn, getTo(i,position[i]))
        return mn
