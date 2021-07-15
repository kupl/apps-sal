class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        for i in range(len(piles) -2, -1, -1):
            piles[i] += + piles[i + 1]
        
        from functools import lru_cache
        @lru_cache(None)
        def takeStone(startInd, M):
            #print(startInd, M)
            if startInd + 2*M>= len(piles):
                return piles[startInd]
            
            bestChoice = float('inf')
            for X in range(1, 2*M + 1):
                newInd = startInd + X
                bestChoice = min(bestChoice, takeStone(newInd, max(X, M)))
            return piles[startInd] - bestChoice
        
        return takeStone(0, 1)
                        

