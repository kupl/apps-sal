class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        INF = float(\"inf\")
        
        dp = [[0]*(N+1) for _ in range(N+1)]
        isComputed = [[False]*(N+1) for _ in range(N+1)]
        
        def getMaxScore(index, M):
            if index == N:
                return 0
            if isComputed[index][M]:
                return dp[index][M]
            
            bestScore = -INF
            
            for X in range(1, 2*M + 1):
                stones = sum(piles[index:index+X])
                score = stones - getMaxScore(min(index+X,N), min(max(M,X),N))
                
                bestScore = max(bestScore,score)
                
                
            isComputed[index][M] = True
            dp[index][M] = bestScore
            
            return bestScore
        
        # total = my score + opponent score
        # delta = my score - opponent score
        total = sum(piles)
        delta = getMaxScore(0,1)
        return (total + delta)//2
        
