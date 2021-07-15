class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddc = evenc = 0
        for i in position:
            if i%2 == 0:
                evenc+=1
            else:
                oddc+=1
        return oddc if oddc <= evenc else evenc
            

