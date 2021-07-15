class Solution:
    
    
    def minFallingPathSum(self, cost: List[List[int]]) -> int:
        
        numHouses = len(cost)
        cols = len(cost[0])
        dp = cost[0]

        for h in range(1, numHouses):
            newRow = [0 for _ in range(cols)]
            for m in range(0, cols):
                newRow[m] = cost[h][m] + min(dp[prevMat]
                    for prevMat in range(0, cols)
                    if prevMat != m)
            dp = newRow

        return min(dp)
