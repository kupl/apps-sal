class Solution:
    def stoneGameII(self, piles: List[int]) -> int:  
        # store (start, M)
        table = {}
        
        def stoneGameRec(start, M):
            if (start, M) in table:
                return table[(start, M)]            
            
            totalTaken = 0
            for i in range(start, min(start + 2 * M, len(piles))):
                totalTaken += piles[i]
                           
            if start + 2 * M >= len(piles):
               return (totalTaken, 0)

            maxStones = (0, 0)
            for i in range(start + 2 * M - 1, start - 1, -1):                    
                X = i - start + 1                            
                theirStones, yourStones = stoneGameRec(i + 1, max(M, X))
                yourStones += totalTaken
                if yourStones > maxStones[0]:
                    maxStones = (yourStones, theirStones)

                totalTaken -= piles[i]

            table[(start, M)] = maxStones
            return maxStones                                                 
                
        alexScore, _ = stoneGameRec(0, 1)                                
        return alexScore

