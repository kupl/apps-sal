class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        self.dp = {}

        def recursiveStoneGame(start, M):            
            if start >= N:
                return 0
            
            # take all if possible
            if N - start <= 2*M:
                return sum(piles[start:])
            
\t\t\t# memoization
            if (start, M) in self.dp:
                return self.dp[(start, M)]

            alex_score = 0
            sum_score = sum(piles[start:])  # all available score
\t\t\t
\t\t\t# explore each x
            for x in range(1, 2*M+1):
\t\t\t    # get opponent's score
                opponent_score = recursiveStoneGame(start+x, max(x, M))
\t\t\t\t# diff is the current palyers score, keep max
                alex_score = max(alex_score, sum_score - opponent_score)
                
            self.dp[(start, M)] = alex_score
                
            return alex_score
        
        
        return recursiveStoneGame(0, 1)
